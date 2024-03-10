// import * as React from "react";
// import Card from "@mui/material/Card";
// import CardContent from "@mui/material/CardContent";
// import CardMedia from "@mui/material/CardMedia";
// import Typography from "@mui/material/Typography";
// import { CardActionArea } from "@mui/material";

// export default function DivItem() {
//   return (
//     <div className="divitem">
//       <a href="/">
//         <Card sx={{ maxWidth: 300 }}>
//           <CardActionArea>
//             <CardMedia
//               component="img"
//               height="200"
//               image="https://via.placeholder.com/150"
//             />
//             <CardContent>
//               <Typography gutterBottom variant="h5" component="div">
//                 Lizard
//               </Typography>
//               <Typography variant="body2" color="text.secondary">
//                 Lizards are a widespread group of squamate reptiles, with over
//                 6,000 species, ranging across all continents except Antarctica
//               </Typography>
//             </CardContent>
//           </CardActionArea>
//         </Card>
//       </a>
//     </div>
//   );
// }

// DivItem.jsx
import React from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Typography from "@mui/material/Typography";
import { CardActionArea } from "@mui/material";
import Image from '../Assets/images/logo-text.png'

const DivItem = ({ item }) => {
  return (
    <div className="divItem" style={{'marginBottom': '1rem'}}>
      <a
        href={
          item.identifier === "place"
            ? `/placedetails/${item.id}`
            : item.identifier === "hotel"
            ? `/hoteldetails/${item.id}`
            : item.identifier === "localevents"
            ? `/localeventdetails/${item.id}`
            : item.identifier === "product"
            ? `/productdetails/${item.id}`
            : item.identifier === "guide"
            ? `/guidedetails/${item.id}`
            : `/`
        }
      >
        <Card sx={{ maxWidth: 300 }}>
          <CardActionArea>
            <CardMedia
              component="img"
              height="200"
              image={item.image} 
              // image={Image}
            />
            <CardContent>
              <Typography gutterBottom variant="h5" component="div">
                {item.name} 
              </Typography>
              <Typography variant="body2" color="text.secondary">
                {item.description}{" "}
              </Typography>
            </CardContent>
          </CardActionArea>
        </Card>
      </a>
    </div>
  );
};

export default DivItem;