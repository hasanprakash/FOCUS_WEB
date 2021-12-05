<template>
  <!-- Carousel -->
    <div class="col-md-12">
        <div class="container-md">
            <div id="carouselExampleCrossfade" class="carousel slide carousel-fade" data-mdb-ride="carousel">
                <div class="carousel-indicators">
                    <button type="button" data-mdb-target="#carouselExampleCrossfade" data-mdb-slide-to="0"
                        class="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-mdb-target="#carouselExampleCrossfade" data-mdb-slide-to="1"
                        aria-label="Slide 2"></button>
                    <button type="button" data-mdb-target="#carouselExampleCrossfade" data-mdb-slide-to="2"
                        aria-label="Slide 3"></button>
                </div>
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="https://images7.alphacoders.com/588/thumb-1920-588644.jpg" class="d-block w-100 " alt="..."
                            style=" height: 600px;" />
                    </div>
                    <div class="carousel-item">
                        <img src="https://www.supercars.net/blog/wp-content/uploads/2020/09/wallpaperflare.com_wallpaper-1-1.jpg"
                            class="d-block w-100" alt="..." style=" height: 600px;" />
                    </div>
                    <div class="carousel-item">
                        <img src="https://wallpaperaccess.com/full/3047149.jpg" class="d-block w-100" alt="..."
                            style=" height: 600px;" />
                    </div>
                </div>
                <button class="carousel-control-prev" type="button" data-mdb-target="#carouselExampleCrossfade"
                    data-mdb-slide="prev">
                    <!-- <span class="carousel-control-prev-icon" aria-hidden="true"></span> -->
                    <font-awesome-icon icon="chevron-left" class="icons" />
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-mdb-target="#carouselExampleCrossfade"
                    data-mdb-slide="next">
                    <!-- <span class="carousel-control-next-icon" aria-hidden="true"></span> -->
                    <font-awesome-icon icon="chevron-right" class="icons" />
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
        </div>
    </div>

    <!-- Carousel -->
</template>

<script>
export default {

}
</script>

<style scoped>
.icons {
    font-size: 40px;
}
.col-md-12 {
    height: auto;
}
img {
    object-fit: cover;
}
</style>