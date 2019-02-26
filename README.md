# Bookstore
*Test task*

The project is in development state, no preparations for deploy were done. 
The project containes **two applications**:
1. Requests - for managing http requests, saving them to the database and displaying last 10 of them in the separate view.
2. Books. Features of this app are:
  * json-formatted fixture with inital data (8 itmes);
  * custom template tag with copyright (start year is defined in settings module);
  * info-logging for pre-save and pre-delete signals on the Book model;
  * custom site admin for books app and separated pages for creating/updating books instances. *NOTE*: all this manipulation can perform only user from 'managers' group. Simplest way to create this group with right permissions and user in it - to run manage command **createmanager**. You can specify username and password as options -n and -p respectively; otherwise defaults ('new_namager'/'not_so_strong_pass') will be used.
  * management command **booksbypublishing** gives ability to see the list of books ordered in ascending or descending direction depending on provided option (-a/-d).

For the Book model only title field is required, because of other of them  are mandatory (price, ISBN) or have some default values (author, publish_date).

In reason of fast creating UI markup *MetroUI* framework was used (via cdn) and no static files provided. MetroUI attributes were added to default Django widgets to customize their behavior and apperance. Somewhere inline css-styles are used for "hot-fixes" of inaccuracies in UI.   