import React from "react";
import "./dataTable.scss";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import { Link } from "react-router-dom";
import CreateOutlinedIcon from '@mui/icons-material/CreateOutlined';
import DeleteForeverOutlinedIcon from '@mui/icons-material/DeleteForeverOutlined';
const DataTable = ({columns,rows}) => {
  

    // const handleDelete = (id)=>{
    //     console.log(id+" has been deleted.")
    //   }

  return (
    <div className="dataTable">
      <DataGrid
        className="dataGrid"
        rows={rows}
        columns={[...columns, {
            field: "actions",
            headerName: "Actions",
            width: 100,
            renderCell: (params)=>{
                return <div className="action">
                  <Link to={`/users/${params.row.id}`}><CreateOutlinedIcon color='success'/></Link>
                  <div className='delete'><DeleteForeverOutlinedIcon color='error'/></div>
                </div>
            }
        }]}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 5,
            },
          },
        }}
        slots={{toolbar:GridToolbar}}
        slotProps={{
            toolbar:{
                showQuickFilter:true,
                quickFilterProps: {debounceMs: 500}
            }
        }}
        pageSizeOptions={[5]}
        checkboxSelection
        disableRowSelectionOnClick
        disableColumnFilter
        disableDensitySelector
        disableColumnSelector
      />
    </div>
  );
};

export default DataTable;
