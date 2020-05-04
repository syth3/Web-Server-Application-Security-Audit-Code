<?php
    use PHPUnit\Framework\TestCase;
    $curr_dir = dirname(__FILE__);
    require_once($curr_dir . '/../src/api.php');

    final class apiSecurityTests extends TestCase {
        public function testCommandInjection() {
            $test_api = new api("create", "test.txt & nc -nlvp 8000", "contents", getcwd() . "/test-output-files");
            $test_api->process_request();
            $this->assertEquals($test_api->file_path, getcwd() . "/test-output-files" . "/test.txt%20%26%20nc%20-nlvp%208000");

        }

        public function testDirectoryTraversal() {
            $test_api = new api("view", "../../../../../../../../../../../etc/passwd", "contents", getcwd() . "/test-output-files");
            $test_api->process_request();
            $this->assertEquals($test_api->file_path, getcwd() . "/test-output-files" . "/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd");
        }
    }

?>