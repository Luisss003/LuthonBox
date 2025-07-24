package com.luisss003.luthonbox.dto;

public class SampleRequest {
    private String base64EncodedFile;
    private String fileName;

    public SampleRequest(String base64EncodedFile, String fileName) {
        this.base64EncodedFile = base64EncodedFile;
        this.fileName = fileName;
    }

    public String getBase64EncodedFile() {
        return base64EncodedFile;
    }

    public void setBase64EncodedFile(String base64EncodedFile) {
        this.base64EncodedFile = base64EncodedFile;
    }

    public String getFileName() {
        return fileName;
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }
}
