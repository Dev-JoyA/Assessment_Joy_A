package com.example.controller;

import com.example.model.Device;
import com.example.model.Reading;
import com.example.service.DeviceService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/devices")
public class DeviceController {

    @Autowired
    private DeviceService deviceService;

    @GetMapping
    public List<Device> getAllDevices() {
        return deviceService.getAllDevices();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Device> getDeviceById(@PathVariable Long id) {
        return deviceService.getDeviceById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public Device addDevice(@RequestBody Device device) {
        return deviceService.addDevice(device);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Device> updateDevice(@PathVariable Long id, @RequestBody Device updatedDevice) {
        return ResponseEntity.ok(deviceService.updateDevice(id, updatedDevice));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteDevice(@PathVariable Long id) {
        deviceService.deleteDevice(id);
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/{id}/readings")
    public List<Reading> getReadingsByDeviceId(@PathVariable Long id) {
        return deviceService.getReadingsByDeviceId(id);
    }

    @PostMapping("/{id}/readings")
    public Reading addReading(@PathVariable Long id, @RequestBody Reading reading) {
        return deviceService.addReading(id, reading);
    }
}
