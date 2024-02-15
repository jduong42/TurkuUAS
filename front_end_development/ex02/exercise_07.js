function convertOuncesToGrams(measurements) {
    const convertedMeasurements = measurements.map(measurement => {
        if (measurement.unit === "ounce") {
            return {
                batchid: measurement.batchid,
                unit: "gram",
                weight: (measurement.weight * 28.3495).toFixed(2)
            }
        } else {
            return measurement;
        }
    });
    return convertedMeasurements;
}

const measurements_1 = [{batchid: 434, unit: "ounce", weight: 12.21 }, 
                        {batchid: 414, unit: "gram", weight: 199.54 },
                        {batchid: 522, unit: "ounce", weight: 18.88 }];

console.log(convertOuncesToGrams(measurements_1)); // [{ batchid: 434, unit: “gram”, weight: 345.86695 },