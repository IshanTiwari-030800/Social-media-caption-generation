import React from 'react';
import CaptionForm from './components/CaptionForm';

function App() {
    return (
        <div className="min-h-screen animated-bg flex flex-col items-center justify-center px-4">
            <div className="text-center">
                <h1 className="text-3xl font-bold mt-8 text-center text-white drop-shadow-lg">
                    📝 Social Media Caption Generator
                </h1>
                <CaptionForm />
            </div>
        </div>
    );
}

export default App;
