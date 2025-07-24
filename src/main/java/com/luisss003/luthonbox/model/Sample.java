package com.luisss003.luthonbox.model;

import java.time.LocalDateTime;

public class Sample {
    private String id;
    private String filePath;
    private LocalDateTime submittedAt;
    private String analysisResult;

    public Sample(String id, String filePath, LocalDateTime submittedAt, String analysisResult) {
        this.id = id;
        this.filePath = filePath;
        this.submittedAt = submittedAt;
        this.analysisResult = analysisResult;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getFilePath() {
        return filePath;
    }

    public void setFilePath(String filePath) {
        this.filePath = filePath;
    }

    public LocalDateTime getSubmittedAt() {
        return submittedAt;
    }

    public void setSubmittedAt(LocalDateTime submittedAt) {
        this.submittedAt = submittedAt;
    }

    public String getAnalysisResult() {
        return analysisResult;
    }

    public void setAnalysisResult(String analysisResult) {
        this.analysisResult = analysisResult;
    }
}
