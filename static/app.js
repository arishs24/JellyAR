document.getElementById('process-video').addEventListener('click', function() {
    let videoFile = document.getElementById('upload-video').files[0];
    if (videoFile) {
        let formData = new FormData();
        formData.append('video', videoFile);

        fetch('/process', {
            method: 'POST',
            body: formData
        })
        .then(response => response.blob())
        .then(blob => {
            let url = URL.createObjectURL(blob);
            let videoElement = document.getElementById('video-preview');
            videoElement.src = url;
            videoElement.onloadeddata = function() {
                // Apply AR effects after the video is loaded and ready to play
                applyAREffects(videoElement);
            };
        })
        .catch(error => console.error('Error:', error));
    }
});

function applyAREffects(videoElement) {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    const geometry = new THREE.BoxGeometry();
    const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    camera.position.z = 5;

    function animate() {
        requestAnimationFrame(animate);
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;
        renderer.render(scene, camera);
    }

    animate();
}
