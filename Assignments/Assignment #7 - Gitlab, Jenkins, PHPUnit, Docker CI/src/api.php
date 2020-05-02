<?php
    class api {
        public $request_method;
        public $request_name;
        public $request_contents;
        public $base_dir;
        public $file_path;

        public function __construct($request_method, $request_name, $request_contents, $base_dir) {
            $this->request_method = $request_method;
            $this->request_name = $request_name;
            $this->request_contents = $request_contents;
            $this->base_dir = $base_dir;
            $this->file_path = $base_dir . "/" . $request_name;
        }

        private function process_create() {
            if (!file_exists($this->base_dir)) {
                mkdir($this->base_dir, 0777, true);
            }
            // Comment line below out to allow for command injection vulnerability
            $this->file_path = $this->file_path = $this->base_dir . "/" . rawurlencode($this->request_name);
            $myfile = fopen($this->file_path, "w");
            fwrite($myfile, $this->request_contents);

            return "File Created\n";
        }

        private function process_del() {
            if (!file_exists($this->file_path)) {
                http_response_code(404);
                return "File Not Found\n";
            }

            unlink($this->file_path);
            return "File Deleted\n";
        }

        private function process_view() {
            // Comment line below out to allow for directory traversal vulnerability
            // Fixed
            $this->file_path = $this->file_path = $this->base_dir . "/" . rawurlencode($this->request_name);
            if (!file_exists($this->file_path)) {
                http_response_code(404);
                return "File Not Found\n";
            }

            return file_get_contents($this->file_path);
        }

        public function process_request() {
            if ($this->request_method == "create") {
                return $this->process_create();
            }
            if ($this->request_method == "del") {
                return $this->process_del();
            }
            if ($this->request_method == "view") {
                return $this->process_view();
            }
            
        }
    }

?>