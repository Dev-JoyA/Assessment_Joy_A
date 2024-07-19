package com.example.service;

import com.example.model.Device;
import com.example.model.Reading;
import com.example.repository.DeviceRepository;
import com.example.repository.ReadingRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class DeviceService {

    @Autowired
    private DeviceRepository deviceRepository;

    @Autowired
    private ReadingRepository readingRepository;

    public List<Device> getAllDevices() {
        return deviceRepository.findAll();
    }

    public Optional<Device> getDeviceById(Long id) {
        return deviceRepository.findById(id);
    }

    public Device addDevice(Device device) {
        return deviceRepository.save(device);
    }

    public Device updateDevice(Long id, Device updatedDevice) {
        return deviceRepository.findById(id)
                .map(device -> {
                    device.setName(updatedDevice.getName());
                    device.setLocation(updatedDevice.getLocation());
                    return deviceRepository.save(device);
                })
                .orElseGet(() -> {
                    updatedDevice.setId(id);
                    return deviceRepository.save(updatedDevice);
                });
    }

    public void deleteDevice(Long id) {
        deviceRepository.deleteById(id);
    }

    public List<Reading> getReadingsByDeviceId(Long id) {
        return readingRepository.findByDeviceId(id);
    }

    public Reading addReading(Long deviceId, Reading reading) {
        return deviceRepository.findById(deviceId)
                .map(device -> {
                    reading.setDevice(device);
                    return readingRepository.save(reading);
                }).orElseThrow(() -> new RuntimeException("Device not found"));
    }
}
