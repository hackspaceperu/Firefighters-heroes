var drawingManager;
var selectedShape;
var emergencyCoordinates;

// Deselect obj
function clearSelection() {
  if (selectedShape) {
    if (selectedShape.type !== 'marker') {
      selectedShape.setEditable(false);
    }

    selectedShape = null;
  }
}

// Select obj
function setSelection(shape) {
  if (shape.type !== 'marker') {
    clearSelection();
    shape.setEditable(true);
  }
  clearSelection();
  selectedShape = shape;
}

// Delete obj
function deleteSelectedShape () {
  if (selectedShape) {
      selectedShape.setMap(null);
  }
}

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 18,
    center: new google.maps.LatLng(52.25097, 20.97114),
    disableDefaultUI: true,
    fullscreenControl: true,
    disableDoubleClickZoom: true,
    zoomControl: true,
    zoomControlOptions: {
      position: google.maps.ControlPosition.LEFT_BOTTOM
    }
  });
  
  drawingManager = new google.maps.drawing.DrawingManager({
    drawingControl: false,
    drawingControlOptions: {
      position: google.maps.ControlPosition.TOP_CENTER
      //drawingModes: ['marker', 'polyline','polygon']
    },
    markerOptions: { draggable: true },
    polygonOptions: {
      strokeWeight: 0,
      fillOpacity: 0.45,
      editable: true,
      draggable: true
    },
    map: map
  });

  $(function(){
    // Events for buttons markers: '.mbtn'
    $('.mbtn').on('click', function(){
      var _this = this;
      // console.log(_this.id);
      if (_this.id !== 'hand') {
        drawingManager.setDrawingMode('marker');
        var markerOptions = drawingManager.get('markerOptions');
        markerOptions.icon = 'img/svg/' + _this.id + '.svg';
        drawingManager.set('markerOptions', markerOptions);
        console.log(markerOptions);
      } else {
        drawingManager.setDrawingMode(null);
      }
      
    });

    // Events for buttons polyline: '.lbtn'
    $('.lbtn').on('click', function(){
      // var _this = this;
      drawingManager.setDrawingMode('polyline');

    });

    // Events for buttons polygon: 'p.btn'
    $('.pbtn').on('click', function(){
      var _this = this;
      if (_this.id === 'section') {
        var polygonOptions = drawingManager.get('polygonOptions');
        polygonOptions.fillColor = '#ff1717';
        drawingManager.set('polygonOptions', polygonOptions);
      }
      if (_this.id === 'section-toxic') {
        var polygonOptions = drawingManager.get('polygonOptions');
        polygonOptions.fillColor = '#000000';
        drawingManager.set('polygonOptions', polygonOptions);
      }
      if (_this.id === 'emergency') {
        var polygonOptions = drawingManager.get('polygonOptions');
        polygonOptions.fillColor = '#ffffff';
        drawingManager.set('polygonOptions', polygonOptions);
      }
      drawingManager.setDrawingMode('polygon');
    });

  });      

  // Overlaycomplete event of the drawingManager object
  // It is unleashed when an object is created on the map
  google.maps.event.addListener(drawingManager, 'overlaycomplete', function (e) { 
    var newShape = e.overlay;

    newShape.type = e.type;

    if (e.type !== google.maps.drawing.OverlayType.MARKER) {
      // Switch back to non-drawing mode after drawing a shape.
      drawingManager.setDrawingMode(null);

      // Add an event listener that selects the newly-drawn shape when the user
      // mouses down on it.
      google.maps.event.addListener(newShape, 'click', function (e) {
        if (e.vertex !== undefined) {
          if (newShape.type === google.maps.drawing.OverlayType.POLYGON) {
            var path = newShape.getPaths().getAt(e.path);
            path.removeAt(e.vertex);
            if (path.length < 3) {
              newShape.setMap(null);
            }
          }
          if (newShape.type === google.maps.drawing.OverlayType.POLYLINE) {
            var path = newShape.getPath();
            path.removeAt(e.vertex);
            if (path.length < 2) {
              newShape.setMap(null);
            }
          }
        }
        // Select the shape in which the click event occurs
        setSelection(newShape);
      });

      google.maps.event.addListener(newShape, 'dblclick', function (e) {
        if (newShape.type === google.maps.drawing.OverlayType.POLYGON) {
          console.log('poly');
          // Add logic for view change
        }
      });

      // Select the shape created instantly
      setSelection(newShape);
    }
    else {
      google.maps.event.addListener(newShape, 'click', function (e) {
        setSelection(newShape);
      });
      setSelection(newShape);
    }
  });

  // Cancels the selection when the drawing mode is changed
  google.maps.event.addListener(drawingManager, 'drawingmode_changed', clearSelection);
  // Cancel the selection when you click
  google.maps.event.addListener(map, 'click', clearSelection);
  // Delete map objects
  google.maps.event.addDomListener(document.getElementById('delete'), 'click', deleteSelectedShape);


  //SEARCH
  // Create the search box and link it to the UI element
  var input = document.getElementById('pac-input');
  var searchBox = new google.maps.places.SearchBox(input);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

  map.addListener('bounds_changed', function () {
    searchBox.setBounds(map.getBounds());
  });
  var markers = [];
  searchBox.addListener('places_changed', function () {
    var places = searchBox.getPlaces();

    if (places.length == 0) {
      return;
    }

    // Clear out the old markers.
    markers.forEach(function (marker) {
      marker.setMap(null);
    });
    markers = [];

    // For each place, get the icon, name and location.
    var bounds = new google.maps.LatLngBounds();
    places.forEach(function (place) {
      if (!place.geometry) {
        console.log("Returned place contains no geometry");
        return;
      }
      var icon = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25)
      };

      // Create a marker for each place.
      markers.push(new google.maps.Marker({
        map: map,
        icon: icon,
        title: place.name,
        position: place.geometry.location
      }));

      emergencyCoordinates = markers[0].getPosition().toJSON();
      console.log(emergencyCoordinates);

      if (place.geometry.viewport) {
        // Only geocodes have viewport.
        bounds.union(place.geometry.viewport);
      } else {
        bounds.extend(place.geometry.location);
      }
    });
    map.fitBounds(bounds);
  });
  //End search

  
  // End initMap()
}
