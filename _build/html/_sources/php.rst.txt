.. _php:

PHP
============

Security Points
------------------
* Avoid using mysql(i)_ extensions **use PDO**
* You should use below code at the time uploading file.

   ``$file = basename(realpath($_GET['file']));``   
* use password_hash and password_verify

   ``$hash = password_hash($password, PASSWORD_DEFAULT);``
   ``password_verify($password, $hash);`` 
 
* Don't Do This

   ``<a href="http://example.com" target="_blank">Click here</a>``
   Do This Instead
   
   ``<a href="https://example.com" target="_blank" rel="noopener noreferrer">Click here</a>``

SANITIZE user data
------------------

.. note:: use below filer

   ``filter_var($_REQUEST['search'], FILTER_SANITIZE_FULL_SPECIAL_CHARS);`` 
   ``filter_var($email_address, FILTER_VALIDATE_EMAIL);`` For Validate email address
   ``filter_var($ip_address, FILTER_VALIDATE_IP);`` For Validate An IP Address
   ``filter_var($url, FILTER_VALIDATE_URL);`` For Validate Url address



PHP.INI Setting 
---------------

.. note:: 

   * Change expose_php to Off
   * Change mail.add_x_header to Off
   * Change session.cookie_httponly to On
      ``session.cookie_httponly = On``
   * Change session.cookie_secure to On
      ``session.cookie_secure = On``
   * Change session.use_strict_mode to On
      ``session.use_strict_mode = 1``
   *  ``allow_url_include = Off``     
   * Change open_basedir
      ``open_basedir = /var/www/html/``
      ``// Multiple directories can be specified with the ":" delimiter``
      ``open_basedir = /var/www/html/:/var/www/html2/:/var/www/html3/``

   * Change upload_temp_dir
      ``upload_tmp_dir = /var/www/html/tmp/``


**Write PHP Error on a Specific IP**

.. code-block:: bash

   if($_SERVER["REMOTE_ADDR"] =='xxx.xxxx.xxx.xxx'){
     error_reporting(E_ALL);
      ini_set('display_errors','Off');
      ini_set("log_errors", 1);
      ini_set("error_log", "D:/xampp/htdocs/live/errors/lservererror.html");
   }

**Write a text file**

.. code-block:: bash

   ##Generate file##
   $arrayInfo =array();
   $path = "/var/www/html/";
   $fp = fopen($path."arrayDetails.txt", "a");
   fwrite($fp, print_r($arrayInfo,true));
   fclose($fp);