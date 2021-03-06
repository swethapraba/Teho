// Client ID and API key from the Developer Console
var CLIENT_ID = '430182679698-2tibecli2mgd2dc3o0gqn763sv8ivm7k.apps.googleusercontent.com';
var API_KEY = 'AIzaSyC-_9wU92HAYjlRNkdJLamccGgcWR4q6aA';

// Array of API discovery doc URLs for APIs used by the quickstart
var DISCOVERY_DOCS = ["https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest"];

// Authorization scopes required by the API; multiple scopes can be
// included, separated by spaces.
var SCOPES = "https://www.googleapis.com/auth/calendar";

var authorizeButton = $('#authorize-button');
var signoutButton = $('#signout-button');

var titles = [];
var descriptions = [];
var startTimes = [];
var endTimes = [];

var req = new XMLHttpRequest()
req.onreadystatechange = function()
{
    if (req.readyState == 4)
    {
        if (req.status != 200)
        {
            //error handling code here
        }
        else
        {
        }
    }
}

/**
 *  On load, called to load the auth2 library and API client library.
 */
function handleClientLoad() {
  gapi.load('client:auth2', initClient);
}

/**
 *  Initializes the API client library and sets up sign-in state
 *  listeners.
 */
function initClient() {
  gapi.client.init({
    apiKey: API_KEY,
    clientId: CLIENT_ID,
    discoveryDocs: DISCOVERY_DOCS,
    scope: SCOPES
  }).then(function () {
    // Listen for sign-in state changes.
    gapi.auth2.getAuthInstance().isSignedIn.listen(updateSigninStatus);

    // Handle the initial sign-in state.
    updateSigninStatus(gapi.auth2.getAuthInstance().isSignedIn.get());
    authorizeButton.onclick = handleAuthClick;
    signoutButton.onclick = handleSignoutClick;
  });
}

/**
 *  Called when the signed in status changes, to update the UI
 *  appropriately. After a sign-in, the API is called.
 */
function updateSigninStatus(isSignedIn) {
  if (isSignedIn) {
    authorizeButton.css("display", "none");
    signoutButton.css("display", "block");
    //loadDayEvents();
  } else {
    authorizeButton.css("display", "none");
    signoutButton.css("display", "block");
  }
}

/**
 *  Sign in the user upon button click.
 */
function handleAuthClick(event) {
    gapi.auth2.getAuthInstance().signIn();
}

/**
 *  Sign out the user upon button click.
 */
function handleSignoutClick(event) {
  gapi.auth2.getAuthInstance().signOut();
}

/**
 * Append a pre element to the body containing the given message
 * as its text node. Used to display the results of the API call.
 *
 * @param {string} message Text to be placed in pre element.
 */
function appendPre(message) {
  var pre = document.getElementById('content');
  var textContent = document.createTextNode(message + '\n');
}

/**
 * Function that parses the standard start time into just hours and minutes.
 */
function parseStartTime(time) {
  var value = time.substring(time.indexOf(":")-2, time.indexOf(":")+3);
  appendPre("start "+value);
  return value;
}

/**
 * Function that parses the standard end time into just hours and minutes.
 */
function parseEndTime(time) {
  var value = time.substring(time.indexOf(":")-2, time.indexOf(":")+3);
  appendPre("end "+value);
  return value;
}

/**
 * Print the summary and start datetime/date of the next ten events in
 * the authorized user's calendar. If no events are found an
 * appropriate message is printed.
 */
function loadDayEvents() {
  gapi.client.calendar.events.list({
    'calendarId': 'primary',
    'timeMin': (new Date()).toISOString(),
    'showDeleted': false,
    'singleEvents': true,
    'maxResults': 10,
    'orderBy': 'startTime'
  }).then(function(response) {
    var events = response.result.items;

    if (events.length > 0) {
      for (i = 0; i < events.length; i++) {
        var event = events[i];
        var start = event.start.dateTime.toString();
        var end = event.end.dateTime.toString();
        var parsedStart = parseStartTime(start);
        var parsedEnd = parseEndTime(end);
        if(start.substring(0, start.indexOf("T")) === (end.substring(0, end.indexOf("T")))) {
          titles.push(event.summary);
          descriptions.push(event.description);
          startTimes.push(parsedStart);
          endTimes.push(parsedEnd);
          console.log(event.summary+" "+event.description+" "+parsedStart+" "+parsedEnd);
        }
      }
    }
  }).then(function(response) {
    getTimes(startTimes, endTimes)
  });
}

/**
 * Calls python function to retrieve the available time blocks.
 */
function getTimes(start, end) {
  /*$.ajax({
    url: "/schedule",
    data: {
      'param1': start,
      'param2': end
    },
    type: "POST",
    success: function(response) {
      console.log(response['free_schedule'])
    },
    error: function(error) {
      console.log(error)
    }
  });*/
  /*req.open('POST', '/schedule')
  req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
  var postVars = 'param1='+startTimes+'&param2='+endTimes
  req.send(postVars)*/
  var data = {
    'param1': start,
    'param2': end
  };

  $.ajax({
    url: "http://localhost:5000/schedule/",
    type: "POST",
    data: JSON.stringify(data), 
    success: function(response) {
      console.log(response)
    },
    error: function(error) {
      console.log(error)
    }
  });
}

function callEventAdd()
{
  //var start = new Date('2018-05-28T17:00:00-07:00');
  //var end = new Date('2018-05-28T09:00:00-07:00');
  //var start = "2018-05-28T17:00:00-07:00";
  //var end = "2018-05-28T09:00:00-07:00";
  addEventToCal('meditate','5','www.google.com','2018-05-28T09:00:00-07:00','2018-05-28T17:00:00-07:00','America/Los_Angeles');
}

/**
 * Parameters: take in ________
 * Outcome: add event to GCal with provided specs
 */
//function addEventToCal(activity,duration,url,starting,ending,tzone)
function addEventToCal(activity,duration,url,starting,ending,tzone)
{
  //starting = '2018-02-28T09:00:00-07:00';
  //ending = '2018-02-28T17:00:00-07:00';
  var eventSummary = "Take "+duration+" minutes to "+activity; //'summary' field needs a string.PARAM
  var buildDescript = "Here\'s Teho\'s recommendation for you: " + url; //build string
  var startDate = starting;//'2018-05-28T09:00:00-7:00';
  var endDate = ending; //'2018-05-28T17:00:00-07:00';
  var zone = tzone;//'America/Los_Angeles';
  var event = {
    'summary': eventSummary,
    'description': buildDescript,//
    'colorId': '1',//This or code 3 is the purple shade we want, will have to experiment
    'start':
    {
      'dateTime': startDate,
      'timeZone': zone
    },
    'end': //
    {
      'dateTime': endDate,
      'timeZone': zone
    },
    /**'attendees': [//// we might not need this since just insert to primary calendar. made for sharing
      {'email': 'lpage@example.com'},////
    ],**/
    'reminders': {//double check fyi
      'useDefault': false,// double check that this stops all reminders
      /**'overrides': [// we are not using reminders
      {'method': 'popup', 'minutes': 10}
      ]**/
    }
  };
  var request = gapi.client.calendar.events.insert(
  {
    'calendarId': 'primary',
    'resource': event
  });

  request.execute(function(event)
  {
    appendPre('Event created: ' + event.htmlLink);
  });
}
