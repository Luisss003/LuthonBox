package com.luisss003.luthonbox.controller;

import com.luisss003.luthonbox.dto.SampleRequest;
import com.luisss003.luthonbox.dto.SampleResponse;
import com.luisss003.luthonbox.model.Sample;
import com.luisss003.luthonbox.service.AnalysisService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/analyses")
public class AnalysisController {

    private final AnalysisService analysisService;

    public AnalysisController(AnalysisService analysisService) {
        this.analysisService = analysisService;
    }

    @PostMapping
    public ResponseEntity<SampleResponse> analyze(@RequestBody SampleRequest request) {
        Sample sample = analysisService.analyze(request);
        return ResponseEntity.ok(new SampleResponse(sample.getAnalysisResult(), null));
    }
}
