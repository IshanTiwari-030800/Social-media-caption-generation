import React, { useState } from 'react';
import axios from 'axios';

function CaptionForm() {
    const [image, setImage] = useState(null);
    const [previewURL, setPreviewURL] = useState(null);
    const [option, setOption] = useState('long caption');
    const [caption, setCaption] = useState('');
    const [loading, setLoading] = useState(false);

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        setImage(file);
        if (file){
            const url = URL.createObjectURL(file);
            setPreviewURL(url);
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!image) return alert("Upload an image first.");

        const formData = new FormData();
        formData.append('image', image);
        formData.append('option', option);

        try {
            setLoading(true);
            const response = await axios.post('https://8d72-34-143-197-196.ngrok-free.app/generate', formData);
            setCaption(response.data.caption);
        } catch (error) {
            alert("Error : " + error.response?.data?.error || error.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="max-w-md mx-auto bg-white p-6 rounded-lg shadow-md mt-10 space-y-4">
            <h2 className="text-xl font-semibold mb-2 text-center">Upload an image and choose a caption style</h2>

            <input
                type="file"
                accept="image/*"
                onChange={handleImageChange}
                className="w-full border rounded px-3 py-2"
            />

            {previewURL && (
                <div className="mt-4 text-center">
                    <img
                        src={previewURL}
                        alt="Preview"
                        className="mx-auto max-h-64 rounded shadow-md"
                    />
                </div>
            )}

            <select
                value={option}
                onChange={e => setOption(e.target.value)}
                className="w-full border rounded px-3 py-2"
            >
                <option>long-caption</option>
                <option>short-caption</option>
                <option>hashtag</option>
            </select>

            <button
                type="submit"
                disabled={loading}
                className={`w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 transition ${loading ? "opacity-50 cursor-not-allowed" : ""}`}
            >
                {loading ? "Generating..." : "Generate"}
            </button>

            {caption && (
                <div className="mt-4 bg-gray-100 p-4 rounded">
                    <h3 className="font-semibold">Generated Caption:</h3>
                    <p className="mt-2">{caption}</p>
                </div>
            )}
        </form>
    );
}

export default CaptionForm;
