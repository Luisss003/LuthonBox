package com.luisss003.luthonbox.service;

import com.luisss003.luthonbox.dto.SampleRequest;
import com.luisss003.luthonbox.model.Sample;
import com.luisss003.luthonbox.util.QemuInvoker;
import org.springframework.stereotype.Service;

import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDateTime;
import java.util.Base64;
import java.util.UUID;

@Service
public class AnalysisService {
    private final QemuInvoker qemuInvoker;

    public AnalysisService(QemuInvoker qemuInvoker) {
        this.qemuInvoker = qemuInvoker;
    }

    public Sample analyze(SampleRequest request) {
        try {
            String id = UUID.randomUUID().toString();
            byte[] decodedBytes = Base64.getDecoder().decode(request.getBase64EncodedFile());
            Path tempFile = Files.createTempFile("malware_" + id, "_" + request.getFileName());
            Files.write(tempFile, decodedBytes);

            String result = qemuInvoker.analyzeSample(tempFile);

            return new Sample(id, tempFile.toString(), LocalDateTime.now(), result);

        } catch (Exception e) {
            throw new RuntimeException("Failed to analyze sample: " + e.getMessage(), e);
        }
    }
}
