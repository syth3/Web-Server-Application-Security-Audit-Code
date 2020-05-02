<?php
    use PHPUnit\Framework\TestCase;
    $curr_dir = dirname(__FILE__);
    require_once($curr_dir . '/../src/api.php');

    final class apiMethodTests extends TestCase {

        /**
         * @small
         */
        public function testClassAttributes() {
            $test_api = new api("create", "test.txt", "contents", getcwd() . "/test-output-files");
            $this->assertEquals($test_api->request_method, "create");
            $this->assertEquals($test_api->request_name, "test.txt");
            $this->assertEquals($test_api->request_contents, "contents");
            $this->assertEquals($test_api->base_dir, getcwd() . "/test-output-files");
            $this->assertEquals($test_api->file_path, getcwd() . "/test-output-files" . "/test.txt");            
        }

        /**
         * @small
         */
        public function testCreateMethod() {
            // Test that the file gets created
            $test_api = new api("create", "test.txt", "contents", getcwd() . "/test-output-files");
            $output = $test_api->process_request();
            $this->assertFileExists($test_api->file_path);

            // Check that the file contains the right contents
            $contents = file_get_contents($test_api->file_path);
            $this->assertEquals($contents, "contents");

            // Check output
            $this->assertEquals($output, "File Created\n");

            //Cleanup
            $del_api = new api("del", "test.txt", null, getcwd() . "/test-output-files");
            $output = $del_api->process_request();
        }

        /**
         * @small
         */
        public function testDelMethod() {
            // Test that the file is deleted if present
            $test_api = new api("create", "test.txt", "contents", getcwd() . "/test-output-files");
            $test_api->process_request();
            $del_api = new api("del", "test.txt", null, getcwd() . "/test-output-files");
            $output = $del_api->process_request();
            $this->assertFileNotExists($del_api->file_path);

            // Test that "File Deleted" is returned
            $this->assertEquals($output, "File Deleted\n");
        }

        /**
         * @small
         */
        public function testDelMethod404() {
            $del_api = new api("del", "non-existant.txt", null, getcwd() . "/test-output-files");
            $output = $del_api->process_request();
            $this->assertEquals($output, "File Not Found\n");
            $this->assertEquals(http_response_code(), 404);
        }

        /**
         * @small
         */
        public function testViewMethod() {
            // Test that the proper file contents is returned
            $test_api = new api("create", "test.txt", "contents", getcwd() . "/test-output-files");
            $test_api->process_request();
            $view_api = new api("view", "test.txt", null, getcwd() . "/test-output-files");
            $output = $view_api->process_request();
            $this->assertEquals($output, "contents");
            
            //Cleanup
            $del_api = new api("del", "test.txt", null, getcwd() . "/test-output-files");
            $output = $del_api->process_request();
        }

        /**
         * @small
         */
        public function testViewMethod404() {
            $view_api = new api("view", "non-existant.txt", null, getcwd() . "/test-output-files");
            $output = $view_api->process_request();
            $this->assertEquals($output, "File Not Found\n");
            $this->assertEquals(http_response_code(), 404);
        }
    }

?>