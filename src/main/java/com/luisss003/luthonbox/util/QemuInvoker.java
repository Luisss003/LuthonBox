package com.luisss003.luthonbox.util;

import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.nio.file.Path;

@Service
public class QemuInvoker {
    public String analyzeSample(Path samplePath) {
        try {
            ProcessBuilder builder = new ProcessBuilder(
                    "qemu-system-x86_64",
                    "-snapshot",
                    "-hda", samplePath.toString(),
                    "-nographic", "-m", "512M"
            );
            builder.redirectErrorStream(true);
            builder.directory(new File("/tmp"));

            Process process = builder.start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            StringBuilder output = new StringBuilder();
            String line;

            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }

            int exitCode = process.waitFor();
            return "Exit code: " + exitCode + "\n" + output.toString();

        } catch (Exception e) {
            return "QEMU error: " + e.getMessage();
        }
    }
}
