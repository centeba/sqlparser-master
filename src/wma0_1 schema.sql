CREATE SCHEMA IF NOT EXISTS "public";

CREATE  TABLE c_client_info ( 
	system_id            INT  NOT NULL  ,
	client_name          varchar(256)  NOT NULL  ,
	client_plating       varchar(256)  NOT NULL  ,
	CONSTRAINT pk_client_info PRIMARY KEY ( system_id )
 );

CREATE  TABLE c_user_info ( 
	system_id            INT  NOT NULL  ,
	first_name           varchar(256)  NOT NULL  ,
	last_name            varchar(256)  NOT NULL  ,
	mobile_number        varchar(24)    ,
	mobile_country_code  INT    ,
	CONSTRAINT pk_user_info PRIMARY KEY ( system_id )
 );

CREATE  TABLE c_user_profile ( 
	system_id            INT  NOT NULL  ,
	alternate_email      varchar(256)    ,
	anticipated_retirement_date date    ,
	birthplace           varchar(256)    ,
	birthdate            date    ,
	country_of_cit       varchar(256)    ,
	country_of_origin    varchar(256)    ,
	country_of_residence varchar(256)    ,
	date_of_death        date    ,
	date_of_marriage     date    ,
	is_dependent_till_age NUMERIC(4,2)    ,
	drivers_license      varchar(256)    ,
	edu_level            varchar(256)    ,
	primary_email        varchar(256)    ,
	employer             varchar(256)    ,
	employer_address     varchar(256)    ,
	employment_status    varchar(100)    ,
	govt_id_doc          varchar(100)    ,
	state_of_residence   varchar(10)    ,
	govt_id_doc_num      varchar(100)    ,
	gender               varchar(10)    ,
	user_id              INT  NOT NULL  ,
	CONSTRAINT pk_user_profile PRIMARY KEY ( system_id, user_id ),
	CONSTRAINT fk_c_user_profile_c_user_info FOREIGN KEY ( user_id ) REFERENCES c_user_info( system_id )   
 );

CREATE  TABLE f_acct_balance ( 
	system_id            INT  NOT NULL  ,
	account_id           INT    ,
	avail_bal            NUMERIC(8,4)    ,
	cur_bal              NUMERIC(8,4)    ,
	credit_limit         NUMERIC(8,4)    ,
	name                 varchar(256)    ,
	CONSTRAINT pk_acct_balance PRIMARY KEY ( system_id )
 );

CREATE  TABLE f_acct_positions ( 
	system_id            INT  NOT NULL  ,
	security_id          varchar(100)    ,
	num_quantity         NUMERIC(8,4)    ,
	maturity_date        date    ,
	market_value         NUMERIC(12,4)    ,
	cost_basis           NUMERIC(12,4)    ,
	custodian            INT    ,
	unit_price           NUMERIC(12,4)    ,
	date_acquired        date    ,
	is_annuity           INT DEFAULT 0   ,
	current_yield        NUMERIC(8,4)    ,
	coupon_rate          NUMERIC(8,4)    ,
	annual_income        NUMERIC(8,4)    ,
	factor_curr          NUMERIC(8,8)    ,
	CONSTRAINT pk_acct_positions PRIMARY KEY ( system_id )
 );

CREATE  TABLE f_retirement_rmd_info ( 
	system_id            INT  NOT NULL  ,
	rmd_min_amt          NUMERIC(12,4)    ,
	rmd_min_amt_prevyr   NUMERIC(12,4)    ,
	rmd_dist_date        date    ,
	rmd_distr_begin_date date    ,
	rmd_distr_end_date   date    ,
	rmd_distr_end_prioryr_date date    ,
	rmd_distr_rem        NUMERIC(12,4)    ,
	rmd_distr_rem_prioryr NUMERIC(12,4)    ,
	rmd_distr_type       NUMERIC(4,0)    ,
	CONSTRAINT pk_retirement_rmd_info PRIMARY KEY ( system_id )
 );

CREATE  TABLE f_security_master ( 
	system_id            INT  NOT NULL  ,
	ticker_symbol        varchar(256)  NOT NULL  ,
	cash_equiv           INT DEFAULT 0 NOT NULL  ,
	close_price          NUMERIC(12,8) DEFAULT 0.0 NOT NULL  ,
	close_price_as_of_date date  NOT NULL  ,
	currency_code        char(5)  NOT NULL  ,
	isin                 varchar(256)  NOT NULL  ,
	cusip                varchar(256)  NOT NULL  ,
	ticker               varchar(256)  NOT NULL  ,
	sedol                varchar(256)  NOT NULL  ,
	institution_id       varchar(256)  NOT NULL  ,
	institution_sec_id   varchar(256)  NOT NULL  ,
	proxy_security_id    varchar(256)  NOT NULL  ,
	CONSTRAINT pk_security_master PRIMARY KEY ( system_id )
 );

CREATE  TABLE f_tax_lots ( 
	system_id            INT  NOT NULL  ,
	account_no           varchar(24)    ,
	lot_date             date    ,
	unit_price           NUMERIC(12,4)    ,
	security_id          INT  NOT NULL  ,
	accrued_int          NUMERIC(12,4)    ,
	accrued_income       NUMERIC(12,4)    ,
	yield_curr           NUMERIC(12,2)    ,
	yield_bought         NUMERIC(12,4)    ,
	coupon_rate          NUMERIC(12,4)    ,
	custodian_code       INT    ,
	security_id_external varchar(12)    ,
	num_shares_orig      NUMERIC(12,4)    ,
	currency_local       varchar(4)    ,
	cost_local_tot       NUMERIC(12,4)    ,
	cost_local_adj_tot   NUMERIC(12,4)    ,
	fx_rate_local        NUMERIC(12,4)    ,
	mkt_val_local        NUMERIC(12,4)    ,
	accrued_cash_local   NUMERIC(12,4)    ,
	accrued_shares_local NUMERIC(12,4)    ,
	gain_loss_unrealized_local NUMERIC(12,4)    ,
	gain_loss_unrealized_base NUMERIC(12,4)    ,
	wash_purchase_date   date    ,
	wash_gain_loss_base  NUMERIC(12,4)    ,
	wash_gain_loss_local NUMERIC(12,4)    ,
	ytm_rate             NUMERIC(12,4)    ,
	unit_cost_amt_local  NUMERIC(12,4)    ,
	unit_cost_amt_base   NUMERIC(12,4)    ,
	amort_amt_local      NUMERIC(12,4)    ,
	amort_amt_base       NUMERIC(12,4)    ,
	CONSTRAINT pk_tax_lots PRIMARY KEY ( system_id, security_id ),
	CONSTRAINT fk_f_tax_lots FOREIGN KEY ( security_id ) REFERENCES f_security_master( system_id )   
 );

CREATE  TABLE insurance_positions ( 
	system_id            INT  NOT NULL  ,
	account_id           INT    ,
	carrier              varchar(256)    ,
	policy_num           varchar(24)    ,
	policy_type          varchar(4)    ,
	invested_premium     NUMERIC(12,4)    ,
	mkt_val              NUMERIC(12,4)    ,
	init_cost            NUMERIC(12,4)    ,
	curr_mkt_val         NUMERIC(12,4)    ,
	policy_status        INT    ,
	carrier_code         varchar(8)    ,
	policy_code          varchar(6)    ,
	issue_date           date    ,
	renewal_date_fixed   date    ,
	policy_rate_fixed    NUMERIC(8,4)    ,
	net_death_benefit    NUMERIC(12,4)    ,
	surrender_val        NUMERIC(12,4)    ,
	policy_role          INT    ,
	CONSTRAINT pk_insurance_positions PRIMARY KEY ( system_id )
 );

CREATE  TABLE m_accrued_interest_types ( 
	system_id            INT  NOT NULL  ,
	int_code             INT  NOT NULL  ,
	int_type             varchar(21)    ,
	CONSTRAINT pk_accrued_interest_types PRIMARY KEY ( system_id )
 );

CREATE  TABLE m_acct_types ( 
	system_id            INT  NOT NULL  ,
	acct_category        varchar(256)  NOT NULL  ,
	acct_types           varchar(256)  NOT NULL  ,
	acct_type_desc       varchar(256)    ,
	CONSTRAINT pk_acct_types PRIMARY KEY ( system_id )
 );

CREATE  TABLE m_asset_taxonomy ( 
	system_id            INT  NOT NULL  ,
	level_1              varchar(12)    ,
	level_2              varchar(12)    ,
	level_3              varchar(12)    ,
	descr                varchar(256)    ,
	CONSTRAINT pk_m_asset_taxonomy PRIMARY KEY ( system_id )
 );

CREATE  TABLE m_cash_tran_codes ( 
	system_id            INT  NOT NULL  ,
	tran_type            varchar(256)    ,
	tran_description     varchar(256)    ,
	CONSTRAINT pk_cash_tran_codes PRIMARY KEY ( system_id )
 );

CREATE  TABLE m_currency_codes_iso4217 ( 
	system_id            INT  NOT NULL  ,
	entity               varchar(256)    ,
	currency_name        varchar(256)    ,
	currency_code        varchar(5)    ,
	NUMERIC_code         INT    ,
	CONSTRAINT pk_currency_codes_iso4217 PRIMARY KEY ( system_id )
 );

CREATE  TABLE m_custodian_list ( 
	system_id            INT  NOT NULL  ,
	cust_code            varchar(10)  NOT NULL  ,
	cust_name            varchar(256)  NOT NULL  ,
	CONSTRAINT pk_custodian_list PRIMARY KEY ( system_id )
 );

CREATE  TABLE m_investment_tran_types ( 
 );

CREATE  TABLE m_mf_reinvest_codes ( 
	system_id            INT  NOT NULL  ,
	reinvest_code        INT    ,
	code_description     varchar(48)    ,
	CONSTRAINT pk_meta_mf_reinvest_codes PRIMARY KEY ( system_id )
 );

CREATE  TABLE m_mortgage_types ( 
	system_id            INT  NOT NULL  ,
	loan_type            varchar(256)    ,
	type_desc            varchar(256)    ,
	CONSTRAINT pk_mortgage_types PRIMARY KEY ( system_id )
 );

CREATE  TABLE m_pymt_schedules ( 
	system_id            INT  NOT NULL  ,
	type_code            INT  NOT NULL  ,
	type_desc            varchar(256)    ,
	CONSTRAINT pk_pymt_schedules PRIMARY KEY ( system_id )
 );

CREATE  TABLE m_security_types ( 
	system_id            INT  NOT NULL  ,
	sec_type             varchar(21)    ,
	sec_description      varchar(256)    ,
	CONSTRAINT pk_security_fax PRIMARY KEY ( system_id )
 );

CREATE  TABLE m_student_loan_status ( 
	system_id            INT  NOT NULL  ,
	loan_status          varchar(12)    ,
	loan_status_desc     varchar(256)    ,
	CONSTRAINT pk_l_student_loan_status PRIMARY KEY ( system_id )
 );

CREATE  TABLE p_i_alloc_factors ( 
	system_id            INT  NOT NULL  ,
	alloc_factor         INT    ,
	factor_desc          varchar(24)    ,
	CONSTRAINT pk_alloc_factors PRIMARY KEY ( system_id )
 );

CREATE  TABLE p_i_asset_alloc_types ( 
	system_id            INT  NOT NULL  ,
	aa_type              INT    ,
	aa_type_desc         varchar(12)    ,
	CONSTRAINT pk_asset_alloc_types PRIMARY KEY ( system_id )
 );

CREATE  TABLE p_i_client_billing_rates ( 
	system_id            INT  NOT NULL  ,
	rate_schedule_active INT    ,
	price_group          varchar(256)    ,
	price_group_desc     varchar(256)    ,
	min_aum_band_1       NUMERIC(12,4)    ,
	rate_band_1          NUMERIC(8,4)    ,
	min_aum_band_2       NUMERIC(12,4)    ,
	rate_band_2          NUMERIC(8,4)    ,
	min_aum_band_3       NUMERIC(12,4)    ,
	rate_band_3          NUMERIC(8,4)    ,
	min_aum_band_4       NUMERIC(12,4)    ,
	rate_band_4          NUMERIC(8,4)    ,
	min_aum_band_5       NUMERIC(12,4)    ,
	rate_band_5          NUMERIC(8,4)    ,
	min_aum_band_6       NUMERIC(12,4)    ,
	rate_band_6          NUMERIC(8,4)    ,
	min_aum_band_7       NUMERIC(12,4)    ,
	rate_band_7          NUMERIC(8,4)    ,
	CONSTRAINT pk_client_billing_rates PRIMARY KEY ( system_id )
 );

CREATE  TABLE p_i_products ( 
	system_id            INT  NOT NULL  ,
	strat_name           varchar(100)    ,
	strat_desc           varchar(256)    ,
	strat_code           varchar(12)    ,
	strat_type           INT    ,
	cusip                varchar(256)    ,
	min_inv_amt          NUMERIC(12,4)    ,
	res_rat              INT    ,
	status               INT    ,
	risk_cat             INT    ,
	benchmark_id         INT    ,
	benchmark_date       date    ,
	fee_type             INT    ,
	fee_freq             INT    ,
	asset_classification INT    ,
	mgr_name             varchar(100)    ,
	mkt_cap              NUMERIC(12,4)    ,
	net_exp_ratio        NUMERIC(8,4)    ,
	yield_targeted       INT    ,
	muni_strat           INT    ,
	alt_strat            INT    ,
	bal_strat            INT    ,
	sust_inv             INT    ,
	concentration_flag   INT    ,
	margin_flag          INT    ,
	fee_val              date    ,
	CONSTRAINT pk_strategies PRIMARY KEY ( system_id )
 );

CREATE  TABLE p_i_programs_inv ( 
	system_id            INT  NOT NULL  ,
	prog_code            varchar(8)    ,
	prog_name            varchar(100)    ,
	prog_desc            varchar(256)    ,
	prog_status          INT    ,
	CONSTRAINT pk_programs_inv PRIMARY KEY ( system_id )
 );

CREATE  TABLE p_i_restriction_cat ( 
	system_id            INT    ,
	res_cat              INT    ,
	res_cat_desc         varchar(256),  
	CONSTRAINT pk_p_i_restriction_cat PRIMARY KEY ( system_id )  
 );

CREATE  TABLE p_l_loan_eligibility ( 
	system_id            INT  NOT NULL  ,
	reason_code          varchar(12)    ,
	reason_desc          varchar(256)    ,
	CONSTRAINT pk_p_l_loan_eligibility PRIMARY KEY ( system_id )
 );

CREATE  TABLE c_accounts ( 
	office               varchar(8)  NOT NULL  ,
	account_no           varchar(24)  NOT NULL  ,
	system_id            INT  NOT NULL  ,
	account_type         NUMERIC(2,0)  NOT NULL  ,
	user_id              INT  NOT NULL  ,
	client_id            INT  NOT NULL  ,
	cash_avail           NUMERIC(12,4) DEFAULT 0.0 NOT NULL  ,
	amt_liquid_val       NUMERIC(12,4) DEFAULT 0.0 NOT NULL  ,
	acct_open_bal        NUMERIC(12,4) DEFAULT 0.0 NOT NULL  ,
	monthly_accrue_amt   NUMERIC(12,4)    ,
	acct_close_date      date    ,
	is_external_acct     INT DEFAULT 0 NOT NULL  ,
	external_custodian_id INT    ,
	account_type_classification INT  NOT NULL  ,
	CONSTRAINT pk_accounts PRIMARY KEY ( system_id, user_id, client_id, account_type_classification ),
	CONSTRAINT fk_accounts_user_info FOREIGN KEY ( user_id ) REFERENCES c_user_info( system_id )   
	   
 );

CREATE UNIQUE INDEX unq_system_id ON c_accounts ( system_id );

CREATE  TABLE c_acct_wire_instructions ( 
	system_id            INT  NOT NULL  ,
	currency_code        INT    ,
	aba_num              varchar(12)    ,
	bank_routing_num     varchar(24)    ,
	bank_name            varchar(100)    ,
	bank_address         varchar(100)    ,
	bank_address_2       varchar(100)    ,
	bank_address_3       varchar(100)    ,
	bank_city_name       varchar(100)    ,
	bank_state_code      varchar(10)    ,
	bank_country_code    varchar(4)    ,
	cust_account_id      INT    ,
	cust_account_name    varchar(100)    ,
	fee_tag              varchar(10)    ,
	obi_name             varchar(100)    ,
	obi_account_id       INT    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_acct_wire_instructions PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_c_acct_wire_instructions FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE c_user_communications ( 
	system_id            INT  NOT NULL  ,
	user_id              INT  NOT NULL  ,
	allow_bulk_emails    INT DEFAULT 0   ,
	allow_mail           INT DEFAULT 1   ,
	allow_email          INT DEFAULT 1 NOT NULL  ,
	do_not_call          INT DEFAULT 1   ,
	fax_opt_out          INT DEFAULT 0   ,
	allow_marketing_materials INT DEFAULT 1   ,
	best_call_time_start date    ,
	best_call_time_end   date    ,
	do_not_track         INT    ,
	dont_solicit         INT DEFAULT 1   ,
	dont_geo_track       INT DEFAULT 1   ,
	CONSTRAINT pk_user_communications PRIMARY KEY ( system_id, user_id ),
	CONSTRAINT fk_user_communications FOREIGN KEY ( user_id ) REFERENCES c_user_info( system_id )   
 );

CREATE  TABLE custodian_br_accounts_ext ( 
	system_id            INT  NOT NULL  ,
	attr_acct            varchar(12)    ,
	attr_data            varchar(256)    ,
	attr_data_types      varchar(256)    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_wf_accounts_ext_0 PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_custodian_br_accounts_ext FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE custodian_br_pos_ext ( 
	system_id            INT  NOT NULL  ,
	attr_name            varchar(100)    ,
	attr_data            varchar(256)    ,
	attr_data_type       varchar(256)    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_custodian_wf_tran_ext_0 PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_custodian_br_pos_ext FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE custodian_sc_accounts_ext ( 
	system_id            INT  NOT NULL  ,
	attr_acct            varchar(12)    ,
	attr_data            varchar(256)    ,
	attr_data_types      varchar(256)    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_wf_accounts_ext_1 PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_custodian_sc_accounts_ext FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE custodian_sc_pos_ext ( 
	system_id            INT  NOT NULL  ,
	attr_name            varchar(100)    ,
	attr_data            varchar(256)    ,
	attr_data_type       varchar(256)    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_custodian_wf_tran_ext_1 PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_custodian_sc_pos_ext FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE custodian_wf_accounts_ext ( 
	system_id            INT  NOT NULL  ,
	attr_acct            varchar(12)    ,
	attr_data            varchar(256)    ,
	attr_data_types      varchar(256)    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_wf_accounts_ext PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_custodian_wf_accounts_ext FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE custodian_wf_tran_ext ( 
	system_id            INT  NOT NULL  ,
	attr_name            varchar(100)    ,
	attr_data            varchar(256)    ,
	attr_data_type       varchar(256)    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_custodian_wf_tran_ext PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_custodian_wf_tran_ext FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE f_fi_interest ( 
	system_id            INT  NOT NULL  ,
	account_no           INT  NOT NULL  ,
	accrued_int_base_curr NUMERIC(12,4)    ,
	accrued_int_local_curr NUMERIC(12,4)    ,
	accrued_int_ytd_base_curr NUMERIC(12,4)    ,
	accrued_int_ytd_local_curr NUMERIC(12,4)    ,
	penalty_amt_base_curr NUMERIC(12,4)    ,
	penalty_amt_local_curr NUMERIC(12,4)    ,
	est_yearly_income_base_curr NUMERIC(12,4)    ,
	est_year_income_local_curr NUMERIC(12,4)    ,
	curr_local           INT    ,
	CONSTRAINT pk_f_fi_interest PRIMARY KEY ( system_id, account_no ),
	CONSTRAINT fk_f_fi_interest_c_accounts FOREIGN KEY ( account_no ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE f_margin_call ( 
	system_id            INT  NOT NULL  ,
	account_id           INT  NOT NULL  ,
	date_trade           date    ,
	date_settle          date    ,
	qty_traded           NUMERIC(8,4)    ,
	call_amt             NUMERIC(8,4)    ,
	in_violation         INT    ,
	margin_call_type     INT    ,
	date_extension       date    ,
	date_sellout         date    ,
	CONSTRAINT pk_margin_call PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_f_margin_call_c_accounts FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE f_margin_info ( 
	system_id            INT  NOT NULL  ,
	buying_power_amt     NUMERIC(12,4)    ,
	maint_req_amt        NUMERIC(12,4)    ,
	maint_call_amt       NUMERIC(12,4)    ,
	fed_call_amt         NUMERIC (5,2)   ,
	margin_interest_amt  NUMERIC(12,4)    ,
	closing_mkt_value    NUMERIC(12,4)    ,
	net_worth_equity_pct NUMERIC(8,4)    ,
	debit_balance_amt    NUMERIC(12,4)    ,
	accrued_interest_amt NUMERIC(12,4)    ,
	daily_interest_amt   NUMERIC(12,4)    ,
	reg_t_excess         NUMERIC(12,4)    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_margin_info PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_f_margin_info_c_accounts FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE f_margin_lending_collateral ( 
	system_id            INT  NOT NULL  ,
	margin_req_amt       NUMERIC(12,4)    ,
	mkt_val_security_id  INT  NOT NULL  ,
	acct_type            INT    ,
	security_type        INT    ,
	option_sym_code      varchar(48)    ,
	option_exp_date      date    ,
	is_principal_protected INT    ,
	structured_product   INT    ,
	non_transferable_qty NUMERIC(8,8)    ,
	non_avail_qty        NUMERIC(8,4)    ,
	tot_sec_qty          NUMERIC(8,4)    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_margin_lending_collateral PRIMARY KEY ( system_id, account_id, mkt_val_security_id ),
	CONSTRAINT fk_f_margin_secmaster FOREIGN KEY ( mkt_val_security_id ) REFERENCES f_security_master( system_id )   
 );

CREATE  TABLE f_transaction_info ( 
	system_id            INT  NOT NULL  ,
	date_transaction     date  NOT NULL  ,
	date_effective       date  NOT NULL  ,
	date_trade           date  NOT NULL  ,
	date_settle          date  NOT NULL  ,
	security_id          INT  NOT NULL  ,
	buy_or_sell          INT  NOT NULL  ,
	qty_tran             NUMERIC(12,4) DEFAULT 0.0 NOT NULL  ,
	cancel_tran          NUMERIC(12,4) DEFAULT 0.0 NOT NULL  ,
	exec_price           NUMERIC(12,4) DEFAULT 0.0 NOT NULL  ,
	tran_principal       NUMERIC(12,4) DEFAULT 0 NOT NULL  ,
	tran_interest        NUMERIC(12,4) DEFAULT 0.0 NOT NULL  ,
	tran_commission      NUMERIC(12,4) DEFAULT 0 NOT NULL  ,
	tran_reg_fee         NUMERIC(8,4) DEFAULT 0 NOT NULL  ,
	tran_sec_fee         NUMERIC(8,4) DEFAULT 0 NOT NULL  ,
	tran_post_fee        NUMERIC(8,4) DEFAULT 0 NOT NULL  ,
	tran_tax_fee         NUMERIC(8,4) DEFAULT 0 NOT NULL  ,
	tran_exchange        INT DEFAULT 0 NOT NULL  ,
	tran_broker          INT DEFAULT 0 NOT NULL  ,
	tran_reinvest_code   INT DEFAULT 0 NOT NULL  ,
	tran_redemption_fee  NUMERIC(8,4) DEFAULT 0 NOT NULL  ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_transaction_info PRIMARY KEY ( system_id, account_id, security_id ),
	CONSTRAINT fk_f_secmaster_info FOREIGN KEY ( security_id ) REFERENCES f_security_master( system_id )   
 );

CREATE  TABLE l_card_auth ( 
	system_id            INT  NOT NULL  ,
	card_no              varchar(24)    ,
	auth_response        varchar(8)    ,
	tran_date            date    ,
	auth_amt             NUMERIC(12,4)    ,
	tran_type            INT    ,
	auth_acct_id         varchar(24)    ,
	tran_code            INT    ,
	tran_amt             NUMERIC(12,4)    ,
	settle_amt           NUMERIC(12,4)    ,
	location_code        varchar(12)    ,
	counterparty_name    varchar(256)    ,
	tran_fee             NUMERIC(8,4)    ,
	network_id           varchar(12)    ,
	pos_terminal         varchar(12)    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_l_card_auth PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_l_card_auth_c_accounts FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE l_liabilities ( 
	system_id            INT  NOT NULL  ,
	account_id           INT  NOT NULL  ,
	apr_percent          NUMERIC(8,4)    ,
	apr_type             INT    ,
	bal_subject_to_apr   NUMERIC(8,4)    ,
	interest_charge_amt  NUMERIC(8,4)    ,
	is_overdue           INT DEFAULT 0   ,
	last_pymt_amt        NUMERIC(8,4)    ,
	last_pymt_date       date    ,
	last_stmt_bal        NUMERIC(8,4)    ,
	min_pymt_amt         NUMERIC(8,4)    ,
	CONSTRAINT pk_liabilities PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_l_liabilities_c_accounts FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE l_loan ( 
	system_id            INT  NOT NULL  ,
	account_id           INT  NOT NULL  ,
	loan_type            varchar(12)    ,
	loan_start_date      date    ,
	loan_end_date        date    ,
	monthly_payment      NUMERIC(12,4)    ,
	can_deduct_tax       INT    ,
	orig_principal       NUMERIC(12,4)    ,
	current_principal    NUMERIC(12,4)    ,
	funding_date         date    ,
	interest_rate        NUMERIC(12,4)    ,
	status_of_loan       char(1)    ,
	loan_description     varchar(256)    ,
	loannet_id           varchar(25)    ,
	loannet_product_code varchar(12)    ,
	delinquent_status    char(8)    ,
	penalty_prepay       INT    ,
	loan_product         varchar(8)    ,
	coupon_adjustment_freq varchar(8)    ,
	original_teaser_rate NUMERIC(8,4)    ,
	first_coupon_date_change date    ,
	avail_credit         NUMERIC(12,4)    ,
	charge_off_amt       NUMERIC(12,4)    ,
	curr_interest_due    NUMERIC(12,4)    ,
	curr_loan_bal        NUMERIC(12,4)    ,
	curr_pymt            NUMERIC(12,4)    ,
	curr_principal       NUMERIC(12,4)    ,
	daily_accrual_amt    NUMERIC(12,4)    ,
	amt_in_delinquency   NUMERIC(12,4)    ,
	expected_loss_amt    NUMERIC(12,4)    ,
	prob_of_default      NUMERIC(12,4)    ,
	default_exposure     NUMERIC(12,4)    ,
	tot_interest_paid    NUMERIC(12,4)    ,
	interest_rate_freq   NUMERIC(8,4)    ,
	rate_discount        NUMERIC(8,4)    ,
	late_charge_amt      NUMERIC(8,4)    ,
	late_charge_date     date    ,
	last_maturity_date   date    ,
	total_loan_disbursed NUMERIC(12,4)    ,
	risk_rating          INT    ,
	underwriter          varchar(12)    ,
	last_payment_date    date    ,
	prepay_penalty       INT    ,
	cost_of_funds_rate   NUMERIC(8,4)    ,
	accrual_method       varchar(12)    ,
	payment_freq         varchar(4)    ,
	first_payment_date   date    ,
	fee_type             INT    ,
	finance_charge       NUMERIC(8,4)    ,
	payment_status       INT    ,
	note_type            INT    ,
	index_code           INT    ,
	CONSTRAINT pk_loan PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_l_loan_c_accounts FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE l_loan_mortgage ( 
	system_id            INT  NOT NULL  ,
	account_id           INT  NOT NULL  ,
	current_late_fee     NUMERIC(8,4)    ,
	escrow_balance       NUMERIC(8,4)    ,
	has_pmi              INT DEFAULT 0   ,
	has_prepay_penalty   INT DEFAULT 0   ,
	interest_rate        NUMERIC(8,4)    ,
	rate_type            INT    ,
	last_pymt_amt        NUMERIC(8,4)    ,
	last_pymt_date       date    ,
	loan_type            INT    ,
	loan_term            NUMERIC(8,4)    ,
	maturity_date        date    ,
	down_payment         NUMERIC(8,4)    ,
	monthly_pymt         NUMERIC(8,4)    ,
	addnl_monthly_pymt   NUMERIC(8,4)    ,
	next_monthly_pymt_date date    ,
	origination_date     date    ,
	origination_principal NUMERIC(8,4)    ,
	principal_bal        NUMERIC(8,4)    ,
	address              varchar(256)    ,
	balloon_loan         INT    ,
	heloc_initial_draw   NUMERIC(8,4)    ,
	home_insurance_co    varchar(256)    ,
	appraisal_value      NUMERIC(12,4)    ,
	loan_purpose         INT    ,
	loan_doc_type        INT    ,
	pmi_insurance_code   INT    ,
	CONSTRAINT pk_loan_mortgage PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_l_loan_mortgage_c_accounts FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE l_property ( 
	system_id            INT  NOT NULL  ,
	property_value       NUMERIC(12,4)    ,
	appraised_value      NUMERIC(12,4)    ,
	annual_increase      NUMERIC(4,2)    ,
	property_use         INT    ,
	purchase_date        date    ,
	sale_date            date    ,
	address              varchar(256)    ,
	sale_cost_basis      NUMERIC(12,4)    ,
	sale_tax_rate        NUMERIC(4,2)    ,
	escrow_amt           NUMERIC(12,4)    ,
	taxes_insurance      NUMERIC(8,4)    ,
	escrow_annual_increase NUMERIC(6,4)    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_property PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_l_property_c_accounts FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE l_student_loans ( 
	system_id            INT  NOT NULL  ,
	disbursement_date    date    ,
	guarantor            INT    ,
	account_no_ext       varchar(24)  NOT NULL  ,
	interest_rate_pct    NUMERIC(8,4)  NOT NULL  ,
	is_overdue           INT DEFAULT 0   ,
	last_payment_date    date    ,
	last_payment_amt     NUMERIC(8,8)    ,
	loan_name            varchar(256)    ,
	loan_status          INT  NOT NULL  ,
	end_date             date    ,
	min_payment_amt      NUMERIC(8,4)    ,
	payment_ref_number   varchar(256)    ,
	repayment_plan       INT DEFAULT 0   ,
	servicer_address     varchar(256)    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_student_loans PRIMARY KEY ( system_id, account_id, loan_status ),
	CONSTRAINT fk_l_student_loans_status FOREIGN KEY ( loan_status ) REFERENCES m_student_loan_status( system_id )   
 );

CREATE  TABLE managed_futures ( 
	system_id            INT  NOT NULL  ,
	capital_commit_amt   NUMERIC(12,4)    ,
	contrib_to_date      NUMERIC(12,4)    ,
	rem_contrib_left     NUMERIC(12,4)    ,
	other_contrib_amt    NUMERIC(12,4)    ,
	total_contrib_amt    NUMERIC(12,4)    ,
	estimated_val_amt    NUMERIC(12,4)    ,
	distr_to_date        NUMERIC(12,4)    ,
	redemptions_to_date  NUMERIC(12,4)    ,
	valuation_type       INT    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_managed_futures PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_managed_futures_c_accounts FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE org_acct_ext ( 
	system_id            INT  NOT NULL  ,
	attr_acct            varchar(12)    ,
	attr_data            varchar(256)    ,
	attr_data_types      varchar(256)    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_wf_accounts_ext_2 PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_org_acct_ext_c_accounts FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE org_pos_ext ( 
	system_id            INT  NOT NULL  ,
	attr_name            varchar(100)    ,
	attr_data            varchar(256)    ,
	attr_data_type       varchar(256)    ,
	account_id           INT  NOT NULL  ,
	CONSTRAINT pk_custodian_wf_tran_ext_2 PRIMARY KEY ( system_id, account_id ),
	CONSTRAINT fk_org_pos_ext_c_accounts FOREIGN KEY ( account_id ) REFERENCES c_accounts( system_id )   
 );

CREATE  TABLE p_i_asset_alloc_model ( 
	system_id            INT  NOT NULL  ,
	asset_alloc_type     INT  NOT NULL  ,
	asset_class          INT  NOT NULL  ,
	asset_class_strat    INT    ,
	strat_pct            NUMERIC(8,4)    ,
	model_status         INT    ,
	active_date          date    ,
	model_type           INT    ,
	prog_id              INT    ,
	CONSTRAINT pk_asset_alloc PRIMARY KEY ( system_id, asset_alloc_type, asset_class ),
	CONSTRAINT fk_p_i_asset_class FOREIGN KEY ( asset_class ) REFERENCES m_asset_taxonomy( system_id )   
 );

CREATE  TABLE p_i_asset_alloc_model_0 ( 
	system_id            INT  NOT NULL  ,
	asset_alloc_type     INT  NOT NULL  ,
	asset_class          INT  NOT NULL  ,
	asset_class_strat    INT    ,
	strat_pct            NUMERIC(8,4)    ,
	model_status         INT    ,
	active_date          date    ,
	model_type           INT    ,
	prog_id              INT    ,
	fa                   varchar(25)    ,
	client               varchar(25)    ,
	account_id           INT    ,
	CONSTRAINT pk_asset_alloc_0 PRIMARY KEY ( system_id, asset_alloc_type, asset_class ),
	CONSTRAINT fk_p_i_asset_class_0 FOREIGN KEY ( asset_class ) REFERENCES m_asset_taxonomy( system_id )   
 );

CREATE  TABLE p_i_product_prog ( 
	system_id            INT  NOT NULL  ,
	prog_id              INT  NOT NULL  ,
	product_id           INT  NOT NULL  ,
	product_status       INT    ,
	asset_classification INT    ,
	status_date          date    ,
	prod_fee             NUMERIC(8,4)    ,
	CONSTRAINT pk_strat_prog PRIMARY KEY ( system_id, prog_id, product_id ),
	CONSTRAINT fk_p_i_product_id FOREIGN KEY ( product_id ) REFERENCES p_i_products( system_id )   
 );

CREATE  TABLE p_l_loan_products ( 
	system_id            INT  NOT NULL  ,
	loan_type            varchar(12)    ,
	can_deduct_tax       boolean    ,
	interest_rate        NUMERIC(12,4)    ,
	loan_description     varchar(256)    ,
	penalty_prepay       boolean    ,
	loan_product         varchar(8)    ,
	coupon_adjustment_freq varchar(8)    ,
	original_teaser_rate NUMERIC(8,4)    ,
	first_coupon_change  INT    ,
	expected_loss_amt    NUMERIC(12,4)    ,
	tot_default_exposure NUMERIC(12,4)    ,
	tot_interest_paid    NUMERIC(12,4)    ,
	interest_rate_freq   NUMERIC(8,4)    ,
	rate_discount        NUMERIC(8,4)    ,
	total_loan_disbursed NUMERIC(12,4)    ,
	risk_rating          INT    ,
	underwriter          varchar(12)    ,
	prepay_penalty       boolean    ,
	cost_of_funds_rate   NUMERIC(8,4)    ,
	accrual_method       varchar(12)    ,
	payment_freq         varchar(4)    ,
	fee_type             INT    ,
	finance_charge       NUMERIC(8,4)    ,
	note_type            INT    ,
	index_code           INT    ,
	system_id_001        integer    ,
	user_id              integer    ,
	client_id            integer    ,
	account_type_classification integer    ,
	CONSTRAINT pk_p_l_loan_products PRIMARY KEY ( system_id ),
	CONSTRAINT fk_l_loan_c_accounts_0 FOREIGN KEY (  user_id ) REFERENCES c_accounts(  user_id)   
 );

COMMENT ON TABLE c_client_info IS 'Client and Account Domain:

info on a client. a client can have multiple accounts owned by different people or institutions';

COMMENT ON TABLE c_user_info IS 'Client and Account Domain:

Info about individual persons; logins, first/last name, etc. Could be multiple users accounts to a client relationship.';

COMMENT ON TABLE c_user_profile IS 'Client and Account Domain:

user extended info';

COMMENT ON COLUMN c_user_profile.country_of_cit IS 'country of citizenship';

COMMENT ON COLUMN c_user_profile.is_dependent_till_age IS 'is this person a dependent until a cretain age';

COMMENT ON COLUMN c_user_profile.govt_id_doc IS 'government issued id document:

passport, drivers license, id, ss_card';

COMMENT ON TABLE f_acct_balance IS 'account balance';

COMMENT ON TABLE f_acct_positions IS 'Investments Financial Domain: account holdings/positions

securities positions in an account';

COMMENT ON COLUMN f_acct_positions.is_annuity IS '0 for NO
1 for YES';

COMMENT ON COLUMN f_acct_positions.factor_curr IS 'current factor';

COMMENT ON TABLE f_retirement_rmd_info IS 'Investment Products Financial Domain:

Info about Required Minimum Distribution info for retirement accounts.';

COMMENT ON COLUMN f_retirement_rmd_info.rmd_min_amt IS 'minimum distribution amount required';

COMMENT ON COLUMN f_retirement_rmd_info.rmd_min_amt_prevyr IS 'RMD for last year';

COMMENT ON COLUMN f_retirement_rmd_info.rmd_dist_date IS 'date of distriubution';

COMMENT ON COLUMN f_retirement_rmd_info.rmd_distr_rem IS 'remaining distribution amount left';

COMMENT ON TABLE f_security_master IS 'Investment Products Financial Domain:

master list of securities';

COMMENT ON COLUMN f_security_master.ticker_symbol IS 'ticker';

COMMENT ON COLUMN f_security_master.cash_equiv IS 'it the security a cash equivalent

0 for NO, 1 for Yes';

COMMENT ON COLUMN f_security_master.close_price IS 'closing price in market';

COMMENT ON COLUMN f_security_master.close_price_as_of_date IS 'date of last closing price updated';

COMMENT ON COLUMN f_security_master.institution_id IS 'which institution is this security entry from';

COMMENT ON COLUMN f_security_master.institution_sec_id IS 'security id at the institution its coming from';

COMMENT ON TABLE f_tax_lots IS 'Investments Financial Domain: : Tax Lots

tax lot table';

COMMENT ON COLUMN f_tax_lots.security_id IS 'internal security id';

COMMENT ON COLUMN f_tax_lots.yield_bought IS 'yield when bought';

COMMENT ON COLUMN f_tax_lots.custodian_code IS 'if externally custodied';

COMMENT ON COLUMN f_tax_lots.security_id_external IS 'security id from external source if custodian is outside';

COMMENT ON COLUMN f_tax_lots.ytm_rate IS 'Yield To Maturity';

COMMENT ON COLUMN insurance_positions.policy_role IS 'owner
bene
annuitant';

COMMENT ON TABLE m_accrued_interest_types IS 'diffen accrued interest types:

30-360 Days
30-Actual Days
Actual-360 Days
Actual-Actual
Half Year
Actual/365';

COMMENT ON COLUMN m_accrued_interest_types.int_type IS 'accrued interest type';

COMMENT ON TABLE m_acct_types IS 'account types:

depository:

Checking, savings, hsa, cd, mmkt, paypal, venmo, prepaid_debit_card, cash_mgmt, ebt, credit_card

loan:

auto_loan, business_loan, commercial_loan, construction_loan, consumer_loan, heloc_loan, general_loan, mortgage_loan, overdraft_loan, loc_loan, student_loan, other_loan

investments: 

529_acct, 401k_acct, 403b_acct, 457b_acct, brokerage_acct, 
cash_acct,  ira_acct, crypto_account, annuity_acct, hsa_acct, 
keogh_acct, life_insurance, mfund_acct, pension_plan_acct,
profit_sharing_acct, roth_ira_acct, sep_ira_acct, simple_ira_acct,
stock_plan_acct, trust_acct, ugma_acct, utma_acct, 
var_annuity_acct, hedge_fund_acct, priv_equity_acct
real_estate_acct, alt_assets_acct

Business Entity

Corporation -  INC
Corporation - Retail Banking Institution
Disregarded Entity - LLC
Escrow Account for Trust Alliance Partners
General Partnership - PAR
Government Entity - GOV
Incorporated Non-Profit Org
Limited Liability Company
Limited Partnerships 
Personal Holding Company
Sole Proprietaryship
Unincorporate Association
Captive Insurance
Foreign Related Entities
Insurance
Investment Club Account
Offshore Insurance
Reinsurance Accounts

Education Accounts

Savings for College Accounts
Coverdell ESA
State Tuition Plans

Middle Market/Institutional Accounts

Bank Middle Market Custody
Bank Middle Market DVP
Middle Market Custody
Middle Market DVP

Personal

Community Property
Guardianship Account
Individual
Joint Tenant Survivorship
Tenants by Entirety
Custodian for Minor UGMA
Custodian for Minor UTMA


Retirement

ERISA Plan Held Away
IRA Rollover
IRA Roth
IRA Inherited Roth
IRA Inherited Roth Reminder
IRA Traditional Inherited
IRA Traditional Inherited Remainder
IRA Traditional
Outside custodian IRA
Outside custodian IRA Retirement Plan
RPM Plan Account
RPM Sub Account
SAR SEP Participant
SAR SEP Principla
Self-Directed Retirement Account
SEP Participant
SEP Principal
Simple IRA Participant
Simple IRA Principal
VIP Basic Plan Account
VIP Basic SubAccount
VIP Plus Plan Account
VIP Plus Plan Account

Special Products

business Other
Charity Organization
Incorporated  
Individual
Joint Account
Listed Company
Personal Holdings Company
Sole Proprietaryship
Trust Account
Hard Dollar Fee - Guardianship
Hard Dollar Fee - Incorporated
Hard Dollar Fee - IRO
Hard Dollar Fee Ind
Hard Dollar Fee Religious
Venture Capital Corporation
Venture Capital Joint tentant
Venture Capital Joint Wros
Venture Capital Living Trust
Venture Capital LLC
Venture Capital Partnership
Venture Capital Sole Prop
Venture Capital Incorporated


Trusts and Estates

Charitable Remainder/Lead Trust
Estate Account
International Trust
Irrevocable Life Insurance Trust
Life Tenant
Living Trust
Testamentary Trust
Trust Company Account
Usufruct';

COMMENT ON COLUMN m_acct_types.acct_category IS 'depository
loan
investments';

COMMENT ON COLUMN m_acct_types.acct_type_desc IS 'description of account type';

COMMENT ON TABLE m_asset_taxonomy IS 'Metadata Domain -> Asset Taxonomy

Level 1	Level 2	Level 3	Descr
Cash	Global Cash	Global Cash	mmt, cash deposits
Equities	US Equities	US Large Cap Growth	
Equities	US Equities	US Large Cap Value	
Equities	US Equities	US Mid Cap Growth	
Equities	US Equities	US Mid Cap Value	
Equities	US Equities	US Small Cap Value	
Equities	US Equities	US Eequities Other	
Equities	US Equities	US Large Cap	
Equities	US Equities	US Mid Cap	
Equities	US Equities	US Small Cap  	
Equities	International Equities	International Equities	
Equities	International Equities	Canadian Equities	
Equities	International Equities	European Equties	
Equities	International Equities	Japan Equities	
Equities	International Equities	Asia Pac ex Japan Equities	
Equities	International Equities	International Small Cap Equities	
Equities	International Equities	Israel Equities	
Equities	International Equities	International Equities Other	
Equities	Emerging and Frontier Market Equities	Emerging Market Equities	
Equities	Emerging and Frontier Market Equities	EEMEA Equities	
Equities	Emerging and Frontier Market Equities	Asia Equities	
Equities	Emerging and Frontier Market Equities	Latin America Equities	
Equities	Emerging and Frontier Market Equities	Frontier Markets	
Equities	Emerging and Frontier Market Equities	Emerging Market Equities	
Equities	Global Equities Other	Global Equities Other	
Fixed Income and Preferreds	Ultra Short Term Fixed Income	Ultra Short Term Fixed Income	
Fixed Income and Preferreds	Ultra Short Term Fixed Income	Ultra Short Term Government	
Fixed Income and Preferreds	Ultra Short Term Fixed Income	Ultra Short Term Corporate	
Fixed Income and Preferreds	Ultra Short Term Fixed Income	Ultra Short Term Municipal	
Fixed Income and Preferreds	Ultra Short Term Fixed Income	Ultra Short Term Securitized	
Fixed Income and Preferreds	Short Term Fixed Income	Short Term Fixed Income	
Fixed Income and Preferreds	Short Term Fixed Income	Short Term Government	
Fixed Income and Preferreds	Short Term Fixed Income	Short Term Corporate	
Fixed Income and Preferreds	Short Term Fixed Income	Short Term Municipal	
Fixed Income and Preferreds	Short Term Fixed Income	Short Term Securitized	
Fixed Income and Preferreds	US Fixed Income Tax Exempt	Intermediate Term Municipals	
Fixed Income and Preferreds	US Fixed Income Tax Exempt	Long Term Municipals	
Fixed Income and Preferreds	US Fixed Income Tax Exempt	US Tax Free Core	
Fixed Income and Preferreds	International Fixed Income	International Intermediate Term Government	
Fixed Income and Preferreds	International Fixed Income	International Intermediate Term Corporate	
Fixed Income and Preferreds	International Fixed Income	International Core Fixed Income	
Fixed Income and Preferreds	International Fixed Income	International Securitized	
Fixed Income and Preferreds	Inflation Linked Securities	Inflation Linked Securities	
Fixed Income and Preferreds	Preferred Securities	Preferred Securities	
Fixed Income and Preferreds	High Yield Fixed Income	High Yield Fixed Income	
Fixed Income and Preferreds	High Yield Fixed Income	High Yield Municipal Fixed Income	
Fixed Income and Preferreds	Bank Loans	Bank Loans	
Fixed Income and Preferreds	Emerging Market Fixed Income	Emerging Market Fixed Income	
Fixed Income and Preferreds	Global Fixed Income	Global Fixed Income	
Fixed Income and Preferreds	Global Fixed Income	Global Fixed Income Other	
Alternatives	Real Assets	Real Estate/REITs	
Alternatives	Real Assets	Commodities	
Alternatives	Real Assets	MLP/Energy Infrastructure	
Alternatives	Real Assets	Infrastructure	
Alternatives	Real Assets	Precious Metals	
Alternatives	Real Assets	Real Assets Other	
Alternatives	Absolute Return Assets	Equity Market Neutral	
Alternatives	Absolute Return Assets	Relative Value	
Alternatives	Absolute Return Assets	Unconstrained Fixed Income	
Alternatives	Absolute Return Assets	Credit Long/Short	
Alternatives	Absolute Return Assets	Non-Directional Multi-Manager/FundOfFunds	
Alternatives	Absolute Return Assets	Absolute Return Assets Other	
Alternatives	Equity Hedge Assets	Global Macro	
Alternatives	Equity Hedge Assets	Managed Futures	
Alternatives	Equity Hedge Assets	Multi-Manager/FundOfFunds	
Alternatives	Equity Hedge Assets	Multi Strategy	Long/Short/Equity
Alternatives	Equity Hedge Assets	Multi Strategy	Market Neutral
Alternatives	Equity Hedge Assets	Multi Strategy	Merger Arbitrage
Alternatives	Equity Hedge Assets	Multi Strategy	Convertible Arbitrage
Alternatives	Equity Hedge Assets	Multi Strategy	Event Driven
Alternatives	Equity Hedge Assets	Multi Strategy	Credit
Alternatives	Equity Hedge Assets	Multi Strategy	Fixed Income Arbitrage
Alternatives	Equity Hedge Assets	Multi Strategy	Global Macro
Alternatives	Equity Hedge Assets	Multi Strategy	Short Only
Alternatives	Equity Return Assets	Equity Long/Short	
Alternatives	Equity Return Assets	Event Driven/Credit	
Alternatives	Equity Return Assets	Distressed Credit	
Alternatives	Equity Return Assets	Directional Multi-Manager/Fund of Funds	
Alternatives	Equity Return Assets	Equity Return Assets other	
Alternatives	Private Investments	Private Real Estate	
Alternatives	Private Investments	Private Equity	
Alternatives	Private Investments	Private Credit	
Alternatives	Private Investments	Private Investments Other	
Alternatives	Alternatives Other	Alternatives Other	
Annuities And Insurance	Variable Annuities	Variable Annuities	
Annuities And Insurance	Variable Annuities	Variable Annuities - Living Benefit	
Annuities And Insurance	Variable Annuities	Variable Annuities - Basic Benefit	
Annuities And Insurance	Fixed Annuities	Fixed Annuities	
Annuities And Insurance	Fixed Annuities	Fixed Annuities - Index	
Annuities And Insurance	Fixed Annuities	Fixed Annuities - Rate	
Annuities And Insurance	Life Insurance	Term Life	
Annuities And Insurance	Life Insurance	Whole Life	
Annuities And Insurance	Annuities and Insurace Other	Annuities and Insurace Other	
Structured Investments	Interest Rates	Short Term	
Structured Investments	Interest Rates	Intermediate Term 	
Structured Investments	Interest Rates	Long Term  	
Structured Investments	Interest Rates	Interest Rates Other	
Structured Investments	Equity	Large Cap	
Structured Investments	Equity	Mid Cap	
Structured Investments	Equity	Small Cap	
Structured Investments	Equity	International Equities	
Structured Investments	Equity	Emerging Markets	
Structured Investments	Equity	Equity Short	
Structured Investments	Equity	Equity Intermediate	
Structured Investments	Equity	Equity Long 	
Structured Investments	Equity	Equity Other	
Structured Investments	Foreign Exchange	G10	
Structured Investments	Foreign Exchange	Emerging Markets	
Structured Investments	Foreign Exchange	BRICS	
Structured Investments	Foreign Exchange	FX Short	
Structured Investments	Foreign Exchange	FX Intermediate	
Structured Investments	Foreign Exchange	FX Long	
Structured Investments	Foreign Exchange	FX Other	
Structured Investments	Commodities	Broad Index	Gold/WTI Crude/High Grade Al, Brent Blend, Bloomberg Commodity index
Structured Investments	Commodities	Precious Metals	
Structured Investments	Commodities	Grains	
Structured Investments	Commodities	Base Metals	
Structured Investments	Commodities	Energy	
Structured Investments	Commodities	Soft 	
Structured Investments	Commodities	Commodities Short	
Structured Investments	Commodities	Commodities Intermediate	
Structured Investments	Commodities	Commodities Long	
Structured Investments	Commodities	Commodities Other	
Structured Investments	Hybrid	Hybrid	
Structured Investments	Hybrid	Hybrid Short	
Structured Investments	Hybrid	Hybrid Intermediate	
Structured Investments	Hybrid	Hybrid Long	
Structured Investments	Hybrid	Hybrid Other	
Structured Investments	Credit	Credit  	
Structured Investments	Credit	Investment Grade	
Structured Investments	Credit	High Yield	
Structured Investments	Credit	Credit Short	
Structured Investments	Credit	Credit Intermediate	
Structured Investments	Credit	Credit Long/Short	
Structured Investments	Credit	Credit Other	
Structured Investments	Other 	Other	
Multi Assets	Multi Assets	US Multi Assets	
Multi Assets	Multi Assets	Global Multi Assets	
Other 	Other 	Other';

COMMENT ON COLUMN m_asset_taxonomy.level_2 IS 'level 2 classification';

COMMENT ON TABLE m_cash_tran_codes IS 'Cash Transaction Codes list:

adjustment, atm_deposit, atm_withdrawal, bank_charge,
bill_payment, cash_deposit, cash_withdrawal, cheque, 
direct_debit, interest, card_purchase,
standing_order, acct_transfer';

COMMENT ON COLUMN m_cash_tran_codes.tran_description IS 'description of cash transaction';

COMMENT ON TABLE m_currency_codes_iso4217 IS 'international iso currency codes

varchar(256)	varchar(256)	varchar(256)	integer
Entity	Currency	Alphabetic Code	NUMERIC Code
AFGHANISTAN	Afghani	AFN	971
ÅLAND ISLANDS	Euro	EUR	978
ALBANIA	Lek	ALL	8
ALGERIA	Algerian Dinar	DZD	12
AMERICAN SAMOA	US Dollar	USD	840
ANDORRA	Euro	EUR	978
ANGOLA	Kwanza	AOA	973
ANGUILLA	East Caribbean Dollar	XCD	951
ANTIGUA AND BARBUDA	East Caribbean Dollar	XCD	951
ARGENTINA	Argentine Peso	ARS	32
ARMENIA	Armenian Dram	AMD	51
ARUBA	Aruban Florin	AWG	533
AUSTRALIA	Australian Dollar	AUD	36
AUSTRIA	Euro	EUR	978
AZERBAIJAN	Azerbaijan Manat	AZN	944
BAHAMAS (THE)	Bahamian Dollar	BSD	44
BAHRAIN	Bahraini Dinar	BHD	48
BANGLADESH	Taka	BDT	50
BARBADOS	Barbados Dollar	BBD	52
BELARUS	Belarusian Ruble	BYN	933
BELGIUM	Euro	EUR	978
BELIZE	Belize Dollar	BZD	84
BENIN	CFA Franc BCEAO	XOF	952
BERMUDA	Bermudian Dollar	BMD	60
BHUTAN	Indian Rupee	INR	356
BHUTAN	Ngultrum	BTN	64
BOLIVIA (PLURINATIONAL STATE OF)	Boliviano	BOB	68
BOLIVIA (PLURINATIONAL STATE OF)	Mvdol	BOV	984
BONAIRE, SINT EUSTATIUS AND SABA	US Dollar	USD	840
BOSNIA AND HERZEGOVINA	Convertible Mark	BAM	977
BOTSWANA	Pula	BWP	72
BOUVET ISLAND	Norwegian Krone	NOK	578
BRAZIL	Brazilian Real	BRL	986
BRITISH INDIAN OCEAN TERRITORY (THE)	US Dollar	USD	840
BRUNEI DARUSSALAM	Brunei Dollar	BND	96
BULGARIA	Bulgarian Lev	BGN	975
BURKINA FASO	CFA Franc BCEAO	XOF	952
BURUNDI	Burundi Franc	BIF	108
CABO VERDE	Cabo Verde Escudo	CVE	132
CAMBODIA	Riel	KHR	116
CAMEROON	CFA Franc BEAC	XAF	950
CANADA	Canadian Dollar	CAD	124
CAYMAN ISLANDS (THE)	Cayman Islands Dollar	KYD	136
CENTRAL AFRICAN REPUBLIC (THE)	CFA Franc BEAC	XAF	950
CHAD	CFA Franc BEAC	XAF	950
CHILE	Chilean Peso	CLP	152
CHILE	Unidad de Fomento	CLF	990
CHINA	Yuan Renminbi	CNY	156
CHRISTMAS ISLAND	Australian Dollar	AUD	36
COCOS (KEELING) ISLANDS (THE)	Australian Dollar	AUD	36
COLOMBIA	Colombian Peso	COP	170
COLOMBIA	Unidad de Valor Real	COU	970
COMOROS (THE)	Comorian Franc	KMF	174
CONGO (THE DEMOCRATIC REPUBLIC OF THE)	Congolese Franc	CDF	976
CONGO (THE)	CFA Franc BEAC	XAF	950
COOK ISLANDS (THE)	New Zealand Dollar	NZD	554
COSTA RICA	Costa Rican Colon	CRC	188
CÔTE D''IVOIRE	CFA Franc BCEAO	XOF	952
CROATIA	Euro	EUR	978
CUBA	Cuban Peso	CUP	192
CUBA	Peso Convertible	CUC	931
CURAÇAO	Netherlands Antillean Guilder	ANG	532
CYPRUS	Euro	EUR	978
CZECHIA	Czech Koruna	CZK	203
DENMARK	Danish Krone	DKK	208
DJIBOUTI	Djibouti Franc	DJF	262
DOMINICA	East Caribbean Dollar	XCD	951
DOMINICAN REPUBLIC (THE)	Dominican Peso	DOP	214
ECUADOR	US Dollar	USD	840
EGYPT	Egyptian Pound	EGP	818
EL SALVADOR	El Salvador Colon	SVC	222
EL SALVADOR	US Dollar	USD	840
EQUATORIAL GUINEA	CFA Franc BEAC	XAF	950
ERITREA	Nakfa	ERN	232
ESTONIA	Euro	EUR	978
ESWATINI	Lilangeni	SZL	748
ETHIOPIA	Ethiopian Birr	ETB	230
EUROPEAN UNION	Euro	EUR	978
FALKLAND ISLANDS (THE) [MALVINAS]	Falkland Islands Pound	FKP	238
FAROE ISLANDS (THE)	Danish Krone	DKK	208
FIJI	Fiji Dollar	FJD	242
FINLAND	Euro	EUR	978
FRANCE	Euro	EUR	978
FRENCH GUIANA	Euro	EUR	978
FRENCH POLYNESIA	CFP Franc	XPF	953
FRENCH SOUTHERN TERRITORIES (THE)	Euro	EUR	978
GABON	CFA Franc BEAC	XAF	950
GAMBIA (THE)	Dalasi	GMD	270
GEORGIA	Lari	GEL	981
GERMANY	Euro	EUR	978
GHANA	Ghana Cedi	GHS	936
GIBRALTAR	Gibraltar Pound	GIP	292
GREECE	Euro	EUR	978
GREENLAND	Danish Krone	DKK	208
GRENADA	East Caribbean Dollar	XCD	951
GUADELOUPE	Euro	EUR	978
GUAM	US Dollar	USD	840
GUATEMALA	Quetzal	GTQ	320
GUERNSEY	Pound Sterling	GBP	826
GUINEA	Guinean Franc	GNF	324
GUINEA-BISSAU	CFA Franc BCEAO	XOF	952
GUYANA	Guyana Dollar	GYD	328
HAITI	Gourde	HTG	332
HAITI	US Dollar	USD	840
HEARD ISLAND AND McDONALD ISLANDS	Australian Dollar	AUD	36
HOLY SEE (THE)	Euro	EUR	978
HONDURAS	Lempira	HNL	340
HONG KONG	Hong Kong Dollar	HKD	344
HUNGARY	Forint	HUF	348
ICELAND	Iceland Krona	ISK	352
INDIA	Indian Rupee	INR	356
INDONESIA	Rupiah	IDR	360
INTERNATIONAL MONETARY FUND (IMF) 	SDR (Special Drawing Right)	XDR	960
IRAN (ISLAMIC REPUBLIC OF)	Iranian Rial	IRR	364
IRAQ	Iraqi Dinar	IQD	368
IRELAND	Euro	EUR	978
ISLE OF MAN	Pound Sterling	GBP	826
ISRAEL	New Israeli Sheqel	ILS	376
ITALY	Euro	EUR	978
JAMAICA	Jamaican Dollar	JMD	388
JAPAN	Yen	JPY	392
JERSEY	Pound Sterling	GBP	826
JORDAN	Jordanian Dinar	JOD	400
KAZAKHSTAN	Tenge	KZT	398
KENYA	Kenyan Shilling	KES	404
KIRIBATI	Australian Dollar	AUD	36
KOREA (THE DEMOCRATIC PEOPLE’S REPUBLIC OF)	North Korean Won	KPW	408
KOREA (THE REPUBLIC OF)	Won	KRW	410
KUWAIT	Kuwaiti Dinar	KWD	414
KYRGYZSTAN	Som	KGS	417
LAO PEOPLE’S DEMOCRATIC REPUBLIC (THE)	Lao Kip	LAK	418
LATVIA	Euro	EUR	978
LEBANON	Lebanese Pound	LBP	422
LESOTHO	Loti	LSL	426
LESOTHO	Rand	ZAR	710
LIBERIA	Liberian Dollar	LRD	430
LIBYA	Libyan Dinar	LYD	434
LIECHTENSTEIN	Swiss Franc	CHF	756
LITHUANIA	Euro	EUR	978
LUXEMBOURG	Euro	EUR	978
MACAO	Pataca	MOP	446
NORTH MACEDONIA	Denar	MKD	807
MADAGASCAR	Malagasy Ariary	MGA	969
MALAWI	Malawi Kwacha	MWK	454
MALAYSIA	Malaysian Ringgit	MYR	458
MALDIVES	Rufiyaa	MVR	462
MALI	CFA Franc BCEAO	XOF	952
MALTA	Euro	EUR	978
MARSHALL ISLANDS (THE)	US Dollar	USD	840
MARTINIQUE	Euro	EUR	978
MAURITANIA	Ouguiya	MRU	929
MAURITIUS	Mauritius Rupee	MUR	480
MAYOTTE	Euro	EUR	978
MEMBER COUNTRIES OF THE AFRICAN DEVELOPMENT BANK GROUP	ADB Unit of Account	XUA	965
MEXICO	Mexican Peso	MXN	484
MEXICO	Mexican Unidad de Inversion (UDI)	MXV	979
MICRONESIA (FEDERATED STATES OF)	US Dollar	USD	840
MOLDOVA (THE REPUBLIC OF)	Moldovan Leu	MDL	498
MONACO	Euro	EUR	978
MONGOLIA	Tugrik	MNT	496
MONTENEGRO	Euro	EUR	978
MONTSERRAT	East Caribbean Dollar	XCD	951
MOROCCO	Moroccan Dirham	MAD	504
MOZAMBIQUE	Mozambique Metical	MZN	943
MYANMAR	Kyat	MMK	104
NAMIBIA	Namibia Dollar	NAD	516
NAMIBIA	Rand	ZAR	710
NAURU	Australian Dollar	AUD	36
NEPAL	Nepalese Rupee	NPR	524
NETHERLANDS (THE)	Euro	EUR	978
NEW CALEDONIA	CFP Franc	XPF	953
NEW ZEALAND	New Zealand Dollar	NZD	554
NICARAGUA	Cordoba Oro	NIO	558
NIGER (THE)	CFA Franc BCEAO	XOF	952
NIGERIA	Naira	NGN	566
NIUE	New Zealand Dollar	NZD	554
NORFOLK ISLAND	Australian Dollar	AUD	36
NORTHERN MARIANA ISLANDS (THE)	US Dollar	USD	840
NORWAY	Norwegian Krone	NOK	578
OMAN	Rial Omani	OMR	512
PAKISTAN	Pakistan Rupee	PKR	586
PALAU	US Dollar	USD	840
PANAMA	Balboa	PAB	590
PANAMA	US Dollar	USD	840
PAPUA NEW GUINEA	Kina	PGK	598
PARAGUAY	Guarani	PYG	600
PERU	Sol	PEN	604
PHILIPPINES (THE)	Philippine Peso	PHP	608
PITCAIRN	New Zealand Dollar	NZD	554
POLAND	Zloty	PLN	985
PORTUGAL	Euro	EUR	978
PUERTO RICO	US Dollar	USD	840
QATAR	Qatari Rial	QAR	634
RÉUNION	Euro	EUR	978
ROMANIA	Romanian Leu	RON	946
RUSSIAN FEDERATION (THE)	Russian Ruble	RUB	643
RWANDA	Rwanda Franc	RWF	646
SAINT BARTHÉLEMY	Euro	EUR	978
SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA	Saint Helena Pound	SHP	654
SAINT KITTS AND NEVIS	East Caribbean Dollar	XCD	951
SAINT LUCIA	East Caribbean Dollar	XCD	951
SAINT MARTIN (FRENCH PART)	Euro	EUR	978
SAINT PIERRE AND MIQUELON	Euro	EUR	978
SAINT VINCENT AND THE GRENADINES	East Caribbean Dollar	XCD	951
SAMOA	Tala	WST	882
SAN MARINO	Euro	EUR	978
SAO TOME AND PRINCIPE	Dobra	STN	930
SAUDI ARABIA	Saudi Riyal	SAR	682
SENEGAL	CFA Franc BCEAO	XOF	952
SERBIA	Serbian Dinar	RSD	941
SEYCHELLES	Seychelles Rupee	SCR	690
SIERRA LEONE	Leone	SLL	694
SIERRA LEONE	Leone	SLE	925
SINGAPORE	Singapore Dollar	SGD	702
SINT MAARTEN (DUTCH PART)	Netherlands Antillean Guilder	ANG	532
SISTEMA UNITARIO DE COMPENSACION REGIONAL DE PAGOS "SUCRE"	Sucre	XSU	994
SLOVAKIA	Euro	EUR	978
SLOVENIA	Euro	EUR	978
SOLOMON ISLANDS	Solomon Islands Dollar	SBD	90
SOMALIA	Somali Shilling	SOS	706
SOUTH AFRICA	Rand	ZAR	710
SOUTH SUDAN	South Sudanese Pound	SSP	728
SPAIN	Euro	EUR	978
SRI LANKA	Sri Lanka Rupee	LKR	144
SUDAN (THE)	Sudanese Pound	SDG	938
SURINAME	Surinam Dollar	SRD	968
SVALBARD AND JAN MAYEN	Norwegian Krone	NOK	578
SWEDEN	Swedish Krona	SEK	752
SWITZERLAND	Swiss Franc	CHF	756
SWITZERLAND	WIR Euro	CHE	947
SWITZERLAND	WIR Franc	CHW	948
SYRIAN ARAB REPUBLIC	Syrian Pound	SYP	760
TAIWAN (PROVINCE OF CHINA)	New Taiwan Dollar	TWD	901
TAJIKISTAN	Somoni	TJS	972
TANZANIA, UNITED REPUBLIC OF	Tanzanian Shilling	TZS	834
THAILAND	Baht	THB	764
TIMOR-LESTE	US Dollar	USD	840
TOGO	CFA Franc BCEAO	XOF	952
TOKELAU	New Zealand Dollar	NZD	554
TONGA	Pa’anga	TOP	776
TRINIDAD AND TOBAGO	Trinidad and Tobago Dollar	TTD	780
TUNISIA	Tunisian Dinar	TND	788
TÜRKİYE	Turkish Lira	TRY	949
TURKMENISTAN	Turkmenistan New Manat	TMT	934
TURKS AND CAICOS ISLANDS (THE)	US Dollar	USD	840
TUVALU	Australian Dollar	AUD	36
UGANDA	Uganda Shilling	UGX	800
UKRAINE	Hryvnia	UAH	980
UNITED ARAB EMIRATES (THE)	UAE Dirham	AED	784
UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND (THE)	Pound Sterling	GBP	826
UNITED STATES MINOR OUTLYING ISLANDS (THE)	US Dollar	USD	840
UNITED STATES OF AMERICA (THE)	US Dollar	USD	840
UNITED STATES OF AMERICA (THE)	US Dollar (Next day)	USN	997
URUGUAY	Peso Uruguayo	UYU	858
URUGUAY	Uruguay Peso en Unidades Indexadas (UI)	UYI	940
URUGUAY	Unidad Previsional	UYW	927
UZBEKISTAN	Uzbekistan Sum	UZS	860
VANUATU	Vatu	VUV	548
VENEZUELA (BOLIVARIAN REPUBLIC OF)	Bolívar Soberano	VES	928
VENEZUELA (BOLIVARIAN REPUBLIC OF)	Bolívar Soberano	VED	926
VIET NAM	Dong	VND	704
VIRGIN ISLANDS (BRITISH)	US Dollar	USD	840
VIRGIN ISLANDS (U.S.)	US Dollar	USD	840
WALLIS AND FUTUNA	CFP Franc	XPF	953
WESTERN SAHARA	Moroccan Dirham	MAD	504
YEMEN	Yemeni Rial	YER	886
ZAMBIA	Zambian Kwacha	ZMW	967
ZIMBABWE	Zimbabwe Dollar	ZWL	932
ZZ01_Bond Markets Unit European_EURCO	Bond Markets Unit European Composite Unit (EURCO)	XBA	955
ZZ02_Bond Markets Unit European_EMU-6	Bond Markets Unit European Monetary Unit (E.M.U.-6)	XBB	956
ZZ03_Bond Markets Unit European_EUA-9	Bond Markets Unit European Unit of Account 9 (E.U.A.-9)	XBC	957
ZZ04_Bond Markets Unit European_EUA-17	Bond Markets Unit European Unit of Account 17 (E.U.A.-17)	XBD	958
ZZ06_Testing_Code	Codes specifically reserved for testing purposes	XTS	963
ZZ07_No_Currency	The codes assigned for transactions where no currency is involved	XXX	999
ZZ08_Gold	Gold	XAU	959
ZZ09_Palladium	Palladium	XPD	964
ZZ10_Platinum	Platinum	XPT	962
ZZ11_Silver	Silver	XAG	961';

COMMENT ON COLUMN m_currency_codes_iso4217.entity IS 'country for that currency code';

COMMENT ON COLUMN m_currency_codes_iso4217.currency_name IS 'currency name for that entity';

COMMENT ON COLUMN m_currency_codes_iso4217.currency_code IS 'the code for that currency';

COMMENT ON COLUMN m_currency_codes_iso4217.NUMERIC_code IS 'NUMERIC code for currency';

COMMENT ON TABLE m_custodian_list IS 'list of custodians';

COMMENT ON COLUMN m_custodian_list.cust_code IS 'custodian code';

COMMENT ON COLUMN m_custodian_list.cust_name IS 'name of custodian';

COMMENT ON TABLE m_investment_tran_types IS 'investment transaction types:

Buy Types:

assignment, contribution, buy, buy_to_cover, dividend_reinvestment
longterm_capgain_investment, shortterm_capgain_investment
qualified_dividend, adjustment_dividend, interest_recd
return_of_principal, stock_distribution, pending_credit,

Sell Types:

distribution, exercise, sell, sell_sort, cancel, cash
pending_debit, 

Fee Types:

account_fees, adjustment_dividend
interest_reinvestment
legal_fees
mgmt_fees
12b_1_fees
qualified_dividend
transfer_fee,
mgmt_free
tax_withhold
unqualified_fees
margin_fees
other_fees';

COMMENT ON TABLE m_mf_reinvest_codes IS 'Meta Data:

Mutual Fund ReInvest Codes:

Book Buy Sell
Special Adjustment
Cross Fund Reinvestment
Cross Fund Reinvestment Dividend
Cross Fund Reinvestment Cap Gain - Short Term
Cross Fund Reinvestment Cap Gain - Long Term
Cert Buy Sell
Exchange
Dividend Reinvestment
Cap Gain Short Term Reinvestment
Cap Gain  Long Term Reinvestment
SIP
Merge
Reinvest
Sweep';

COMMENT ON TABLE m_mortgage_types IS 'types of mortgages';

COMMENT ON COLUMN m_mortgage_types.loan_type IS 'conventional
fixed
variable';

COMMENT ON COLUMN m_mortgage_types.type_desc IS 'loan type description';

COMMENT ON TABLE m_pymt_schedules IS 'interest payment schedules:

no interest, annual, semi annual, 3 payments a year, yearly, quarterly, monthly, paid at maturity, irregular, weekly, biweekly, paid at maturity, no pay';

COMMENT ON TABLE m_security_types IS 'security types:

cash, crypto, derivative, equity_stock, etf, equity_option,
fixed_income, loan, mutual_fund, hedge_fund, private_equity

Muni bond
Unspecified
general obligation
revenue
cash

alternatives
farm and timber land
infra
master investment trust
priv equi
real estate

bond
Corporate bond
convertible
govt agency debt
govt agency pass thru
non-agency residential mbs
undefined
bank loans
gov/treasury
warrants/rights call & put
future
corp inflation proteced
commercial mbs
govt agency cmo
govt agency arm
debt swap
interest rate swap / future /forward
credit default swap
total return swap
treasury future
govt inflation protected
bond indexd
Future
option – call
option put
















cash
option put
commercial paper
future offset
repo
option offset
swap offset
forward offset
stable val fund
currency
Future
swap
forward
warrant rights calls [uts
equity
Future
option call / put
equity
undefined
reit
units
income trust
equity swap
index swap
mutual funds
unspecified
close fund
etf
hedge fund
mmkt
open ended
separate account
variable annuity
mf CIT

equity index
options
futures





other
future
property
other assets/liabilities
aset swap
contract for diff
vol swap
warrants
commodity
Futures
options calls/put
preferred
stock
convertible';

COMMENT ON TABLE m_student_loan_status IS 'Lending Domain:

Studen Loan statuses

canceled
charged_off
claim
consolidated
deferment
delinquent
discharged
extention
forbearance
in_grace
in_military
in_school
not_disbursed
paid_in_full
refunded_repayment
transferred';

COMMENT ON COLUMN m_student_loan_status.loan_status_desc IS 'Status Description';

COMMENT ON TABLE p_i_alloc_factors IS 'Table with a list of factors to consider in asset allocation';

COMMENT ON COLUMN p_i_alloc_factors.alloc_factor IS '0 - Risk Tolerance
1 - Time Horizon
2 - Risk Rewards
3 - Investment Goals';

COMMENT ON COLUMN p_i_alloc_factors.factor_desc IS '0 - Risk Tolerance
1 - Time Horizon
2 - Risk Rewards
3 - Investment Goals';

COMMENT ON TABLE p_i_asset_alloc_types IS 'types of asset allocation strategies

0 - Age Based
1 - Lifecycle Based
2 - Tactical
3  - Strategic
4 - Dynamic';

COMMENT ON TABLE p_i_client_billing_rates IS 'Product table for Client Billing Rates';

COMMENT ON COLUMN p_i_client_billing_rates.rate_schedule_active IS 'Is this schedule active or not';

COMMENT ON TABLE p_i_products IS 'list of various strategies available via SMAs, MFs, ETFs';

COMMENT ON COLUMN p_i_products.strat_code IS 'strat code available to search on screens, filtering, etc';

COMMENT ON COLUMN p_i_products.strat_type IS '0 - SMA
1 - Mutual Funds
2 - ETF';

COMMENT ON COLUMN p_i_products.cusip IS 'cusip for MF and ETF';

COMMENT ON COLUMN p_i_products.min_inv_amt IS 'Minimum Investment Amount in this strategy. Mostly for SMAs';

COMMENT ON COLUMN p_i_products.res_rat IS 'Research Rating: 

0 - Recommended
1 - NotRecommended';

COMMENT ON COLUMN p_i_products.status IS 'is strategy available or not

0 - NOT
1 - YES';

COMMENT ON COLUMN p_i_products.risk_cat IS '0 - Conservative
1 - Moderate
2- Aggressive';

COMMENT ON COLUMN p_i_products.benchmark_id IS 'benchmark that the performance of this strategy is measured against. Could be industry standard or custom benchmark';

COMMENT ON COLUMN p_i_products.benchmark_date IS 'start date when this measure started vs benchmark';

COMMENT ON COLUMN p_i_products.fee_type IS '0 - Hard Dollar
1 - Percentage';

COMMENT ON COLUMN p_i_products.fee_freq IS '0 - Monthly
1 - Quarterly
2 - Annually';

COMMENT ON COLUMN p_i_products.mgr_name IS 'Manager Name';

COMMENT ON COLUMN p_i_products.mkt_cap IS 'Market Cap if MF/ETF';

COMMENT ON COLUMN p_i_products.net_exp_ratio IS 'Net Expense Ratio if Mutual Fund / ETF';

COMMENT ON COLUMN p_i_products.yield_targeted IS 'Is  the strategy targeted towards yield

0 - NO
1 - YES';

COMMENT ON COLUMN p_i_products.muni_strat IS 'is the strategy a muni strat

0 - NO
1 - YES';

COMMENT ON COLUMN p_i_products.alt_strat IS 'is it an alternative investment

0 - NO
1 - YES';

COMMENT ON COLUMN p_i_products.bal_strat IS 'Is the strategy a balance strategy

0 - NO
1 - YES';

COMMENT ON COLUMN p_i_products.sust_inv IS 'Is the strategy supporting a sustainable investment goal eg climate change

0 - NO
1 - YES';

COMMENT ON COLUMN p_i_products.concentration_flag IS 'Does the strategy have a concentration of certain assets

0 - NO
1 - YES';

COMMENT ON COLUMN p_i_products.margin_flag IS 'Can you have margin on the strategy

0 - NO
1 - YES';

COMMENT ON TABLE p_i_programs_inv IS 'Programs available to investment in. Typically would be things like: SMAs, UMAs, FA as PM, Self Directed, etc';

COMMENT ON COLUMN p_i_programs_inv.prog_code IS 'code to search/display';

COMMENT ON COLUMN p_i_programs_inv.prog_desc IS 'description of the program';

COMMENT ON COLUMN p_i_programs_inv.prog_status IS 'status of program

0- TERMINATED
1 -  MAINTENANCE (no new accounts)
2 - AVAILABLE';

COMMENT ON TABLE p_i_restriction_cat IS 'restriction categories at program level

need client restrictions table also';

COMMENT ON COLUMN p_i_restriction_cat.res_cat IS 'Restriction Category:

eg 

Tobacco
Firearms
etc';

COMMENT ON COLUMN p_i_restriction_cat.res_cat_desc IS 'Description of restriction category';

COMMENT ON TABLE p_l_loan_eligibility IS 'Product Info for Lending Products Domain -> Criteria for Loan Eligibility

total client aum
aum eligible
aum eligible cash equiv
aum eligible equity
aum eligible fixed income
aum eligible other
amt sbp pledged estimate
amt net acquired assets 12 month
amt total assets
amt total withdrawn ytd';

COMMENT ON TABLE c_accounts IS 'Client and Account Domain:

Information on Retail WM Accounts';

COMMENT ON COLUMN c_accounts.account_type IS '0 - cash
1- margin
2 - short
3- loan';

COMMENT ON COLUMN c_accounts.amt_liquid_val IS 'value of account if uncovered options not factored in';

COMMENT ON COLUMN c_accounts.is_external_acct IS '0 for NO, 1 for YES';

COMMENT ON TABLE c_acct_wire_instructions IS 'Client and Account Domain:

Wire instructions for client account';

COMMENT ON COLUMN c_acct_wire_instructions.currency_code IS 'currency code for wire';

COMMENT ON COLUMN c_acct_wire_instructions.aba_num IS 'bank aba num';

COMMENT ON COLUMN c_acct_wire_instructions.cust_account_id IS 'account id for receiving party';

COMMENT ON COLUMN c_acct_wire_instructions.obi_name IS 'Message to Beneficiary name';

COMMENT ON TABLE c_user_communications IS 'Client and Account Domain:

For WM Clients what are the details behind how the user/client want to be communicated with.';

COMMENT ON COLUMN c_user_communications.allow_bulk_emails IS 'Allow Marketing/Bulk emails

0 for NO, 1 for Yes';

COMMENT ON COLUMN c_user_communications.allow_mail IS 'Allow Postal Mail or not

1 for Yes, 0 for No';

COMMENT ON COLUMN c_user_communications.allow_email IS '1 for Yes, 0 for No';

COMMENT ON COLUMN c_user_communications.do_not_call IS 'Cold calling for new biz/leads

0 for Don''t call, 1 for Allow calls';

COMMENT ON COLUMN c_user_communications.fax_opt_out IS 'opt out of faxes

0 for NO faxes, 1 for Yes to faxes';

COMMENT ON COLUMN c_user_communications.allow_marketing_materials IS 'Ok to send marketing materials or not

0 for No, 1 for Yes';

COMMENT ON COLUMN c_user_communications.best_call_time_start IS 'Best time to call - Start Time';

COMMENT ON COLUMN c_user_communications.do_not_track IS 'do not track on apps/online

0 to No tracking, 1 for Ok to Track';

COMMENT ON COLUMN c_user_communications.dont_solicit IS 'don''t solicit for new biz

0 for don''t, 1 for Ok to solicit';

COMMENT ON COLUMN c_user_communications.dont_geo_track IS 'don''t track location

0 for don''t track, 1 for ok to track';

COMMENT ON TABLE custodian_br_accounts_ext IS 'Extension table for Broadridge (BR) custodian for data that doesn''t fit into the core tables.

This is for account related data only';

COMMENT ON COLUMN custodian_br_accounts_ext.attr_acct IS 'attribute name';

COMMENT ON COLUMN custodian_br_accounts_ext.attr_data IS 'store as json';

COMMENT ON COLUMN custodian_br_accounts_ext.attr_data_types IS 'data type of the attribute. store as json';

COMMENT ON TABLE custodian_br_pos_ext IS 'extension table for positions info for custodian Broadridge';

COMMENT ON COLUMN custodian_br_pos_ext.attr_name IS 'name of attribute';

COMMENT ON COLUMN custodian_br_pos_ext.attr_data IS 'whats the data. Store in JSON format';

COMMENT ON COLUMN custodian_br_pos_ext.attr_data_type IS 'store attribute data as JSON';

COMMENT ON TABLE custodian_sc_accounts_ext IS 'Extension table for Schwab (SC) custodian for data that doesn''t fit into the core tables.

This is for account related data only';

COMMENT ON COLUMN custodian_sc_accounts_ext.attr_acct IS 'attribute name';

COMMENT ON COLUMN custodian_sc_accounts_ext.attr_data IS 'store as json';

COMMENT ON COLUMN custodian_sc_accounts_ext.attr_data_types IS 'data type of the attribute. store as json';

COMMENT ON TABLE custodian_sc_pos_ext IS 'extension table for positions info for custodian Schwab';

COMMENT ON COLUMN custodian_sc_pos_ext.attr_name IS 'name of attribute';

COMMENT ON COLUMN custodian_sc_pos_ext.attr_data IS 'whats the data. Store in JSON format';

COMMENT ON COLUMN custodian_sc_pos_ext.attr_data_type IS 'store attribute data as JSON';

COMMENT ON TABLE custodian_wf_accounts_ext IS 'Extension table for Wells Fargo (WF)  custodian for data that doesn''t fit into the core tables.

This is for account related data only';

COMMENT ON COLUMN custodian_wf_accounts_ext.attr_acct IS 'attribute name';

COMMENT ON COLUMN custodian_wf_accounts_ext.attr_data IS 'store as json';

COMMENT ON COLUMN custodian_wf_accounts_ext.attr_data_types IS 'data type of the attribute. store as json';

COMMENT ON TABLE custodian_wf_tran_ext IS 'extension table for transaction info for custodian Wells Fargo';

COMMENT ON COLUMN custodian_wf_tran_ext.attr_name IS 'name of attribute';

COMMENT ON COLUMN custodian_wf_tran_ext.attr_data IS 'whats the data. Store in JSON format';

COMMENT ON COLUMN custodian_wf_tran_ext.attr_data_type IS 'store attribute data as JSON';

COMMENT ON TABLE f_fi_interest IS 'Financial Transactions Domain: Fixed Income Interest accruals';

COMMENT ON COLUMN f_margin_call.margin_call_type IS 'Fed Call, Min Equity Call, Brokerage Call, NYSE call';

COMMENT ON TABLE f_margin_info IS 'Investment Products Financial Domain:

account margin info';

COMMENT ON COLUMN f_margin_info.maint_req_amt IS 'amt equity needed for margin';

COMMENT ON COLUMN f_margin_info.maint_call_amt IS 'amt due when equity below reqs of exchange';

COMMENT ON COLUMN f_margin_info.fed_call_amt IS 'amt due to cover trading activity based on margin pct';

COMMENT ON COLUMN f_margin_info.margin_interest_amt IS 'margin interest rate';

COMMENT ON COLUMN f_margin_info.debit_balance_amt IS 'amt owed by acct';

COMMENT ON COLUMN f_margin_info.accrued_interest_amt IS 'cumulative interest on margin loan';

COMMENT ON COLUMN f_margin_info.daily_interest_amt IS 'daily interest on margin loan';

COMMENT ON COLUMN f_margin_info.reg_t_excess IS 'amt available for margin to client';

COMMENT ON TABLE f_margin_lending_collateral IS 'Investment Products Financial Domain:

collateral for margin requirements';

COMMENT ON COLUMN f_margin_lending_collateral.acct_type IS 'margin(purpose), margin(non p), cash';

COMMENT ON COLUMN f_margin_lending_collateral.structured_product IS 'YES, NO (0)';

COMMENT ON COLUMN f_margin_lending_collateral.non_transferable_qty IS 'qty that can''t be sold or moved out';

COMMENT ON COLUMN f_margin_lending_collateral.non_avail_qty IS 'qty that can''t be sold or moved out';

COMMENT ON TABLE f_transaction_info IS 'Investment Products Financial Domain:

table with transactions info';

COMMENT ON COLUMN f_transaction_info.buy_or_sell IS '0 for BUY, 1 for SELL';

COMMENT ON COLUMN f_transaction_info.qty_tran IS 'transaction quantity';

COMMENT ON COLUMN f_transaction_info.cancel_tran IS 'quantity canceled';

COMMENT ON COLUMN f_transaction_info.tran_commission IS 'transaction commission';

COMMENT ON COLUMN f_transaction_info.tran_post_fee IS 'postage fee';

COMMENT ON COLUMN f_transaction_info.tran_tax_fee IS 'tax fee';

COMMENT ON COLUMN f_transaction_info.tran_exchange IS 'exchange id';

COMMENT ON COLUMN f_transaction_info.tran_broker IS 'opposing broker id';

COMMENT ON TABLE l_card_auth IS 'Lending Domain: Card (Debit/Credit) Authorization Info';

COMMENT ON COLUMN l_card_auth.tran_type IS '0 - debit/buy
1 - credit/sell';

COMMENT ON COLUMN l_card_auth.auth_acct_id IS 'processor acct no';

COMMENT ON COLUMN l_card_auth.tran_code IS 'Return
ATM
Purchase';

COMMENT ON COLUMN l_card_auth.location_code IS 'Location code from processor for where the card was swiped';

COMMENT ON COLUMN l_card_auth.counterparty_name IS 'merchant, etc';

COMMENT ON COLUMN l_liabilities.bal_subject_to_apr IS 'balance subject to apr';

COMMENT ON COLUMN l_liabilities.is_overdue IS '0 for NO
1 for YES';

COMMENT ON COLUMN l_liabilities.last_stmt_bal IS 'last statement balance';

COMMENT ON TABLE l_loan IS 'Lending Domain:

generic loan model';

COMMENT ON COLUMN l_loan.loan_type IS 'student, auto, cc, sbl, personal, loc, mortgage, other';

COMMENT ON COLUMN l_loan.can_deduct_tax IS '0 for NO, 1 for YES';

COMMENT ON COLUMN l_loan.delinquent_status IS '30,60,90,current';

COMMENT ON COLUMN l_loan.penalty_prepay IS '0 for NO, 1 for YES';

COMMENT ON COLUMN l_loan.total_loan_disbursed IS 'if HELOC';

COMMENT ON COLUMN l_loan.prepay_penalty IS '0 for NO, 1 for YES';

COMMENT ON COLUMN l_loan.note_type IS 'revolving credit
fixed term loan
letter of credit';

COMMENT ON COLUMN l_loan.index_code IS 'libor 30 etc';

COMMENT ON TABLE l_loan_mortgage IS 'Lending Domain:

mortgage loan';

COMMENT ON COLUMN l_loan_mortgage.has_pmi IS 'PMI - private mortgage insurance

0 for NO
1 for Yes';

COMMENT ON COLUMN l_loan_mortgage.has_prepay_penalty IS 'prepayment penalty

0 for NO
1 for YES';

COMMENT ON COLUMN l_loan_mortgage.rate_type IS 'interest rate type';

COMMENT ON COLUMN l_loan_mortgage.principal_bal IS 'principal balance';

COMMENT ON COLUMN l_loan_mortgage.address IS 'property address';

COMMENT ON COLUMN l_loan_mortgage.balloon_loan IS '0 for NO, 1 for YES';

COMMENT ON COLUMN l_loan_mortgage.loan_purpose IS 'purchase
refi
cashout';

COMMENT ON COLUMN l_loan_mortgage.loan_doc_type IS 'nodoc
full
full/alt';

COMMENT ON TABLE l_property IS 'Lending Domain:

property info';

COMMENT ON COLUMN l_property.annual_increase IS 'annual increase in appreciation  as a percentage';

COMMENT ON COLUMN l_property.property_use IS 'first home
second home
vacation
investment';

COMMENT ON TABLE l_student_loans IS 'Lending Domain:

Table with Student Loan information';

COMMENT ON COLUMN l_student_loans.guarantor IS 'person who is guaranteeing the student loan';

COMMENT ON COLUMN l_student_loans.account_no_ext IS 'account number at external provider of student loans';

COMMENT ON COLUMN l_student_loans.is_overdue IS 'is payment overdue

0 for NO, 1 for Yes';

COMMENT ON COLUMN l_student_loans.end_date IS 'end date for loan';

COMMENT ON COLUMN l_student_loans.repayment_plan IS '0 for NO, 1 for YES';

COMMENT ON COLUMN l_student_loans.servicer_address IS 'loan servicing company address';

COMMENT ON COLUMN managed_futures.estimated_val_amt IS 'HF/FO funds';

COMMENT ON COLUMN managed_futures.valuation_type IS 'estimated
final
audited';

COMMENT ON TABLE org_acct_ext IS 'Extension table for extra info that client org wants to store thats not part of core data model

This is for account related data only';

COMMENT ON COLUMN org_acct_ext.attr_acct IS 'attribute name';

COMMENT ON COLUMN org_acct_ext.attr_data IS 'store as json';

COMMENT ON COLUMN org_acct_ext.attr_data_types IS 'data type of the attribute. store as json';

COMMENT ON TABLE org_pos_ext IS 'extension table for positions  info for the client/org that doesn''t fit into core data model';

COMMENT ON COLUMN org_pos_ext.attr_name IS 'name of attribute';

COMMENT ON COLUMN org_pos_ext.attr_data IS 'whats the data. Store in JSON format';

COMMENT ON COLUMN org_pos_ext.attr_data_type IS 'store attribute data as JSON';

COMMENT ON TABLE p_i_asset_alloc_model IS 'Table of asset allocation models for the institution';

COMMENT ON COLUMN p_i_asset_alloc_model.asset_alloc_type IS 'Allocation Model Type: from asset allocation model type table';

COMMENT ON COLUMN p_i_asset_alloc_model.asset_class IS 'Asset Allocation Class; from asset class Meta Data types';

COMMENT ON COLUMN p_i_asset_alloc_model.asset_class_strat IS 'what product does this hold (from table of products) or a cusip if its not a SMA/ETF/MF available for that program

One asset class can have multipe stategies. eg Equity can have multiple equity holdings';

COMMENT ON COLUMN p_i_asset_alloc_model.strat_pct IS 'percentage of that strategy. Total asset allocation model totals to a 100%';

COMMENT ON COLUMN p_i_asset_alloc_model.model_status IS '0 - TERMINATED
1 - ACTIVE
2 - ON HOLD';

COMMENT ON COLUMN p_i_asset_alloc_model.active_date IS 'Date this model was or will be activated';

COMMENT ON COLUMN p_i_asset_alloc_model.model_type IS '0 - new money
1 - existing accounts';

COMMENT ON COLUMN p_i_asset_alloc_model.prog_id IS 'what program is this allocation available in?';

COMMENT ON TABLE p_i_asset_alloc_model_0 IS 'Table of asset allocation models for the institution';

COMMENT ON COLUMN p_i_asset_alloc_model_0.asset_alloc_type IS 'Allocation Model Type: from asset allocation model type table';

COMMENT ON COLUMN p_i_asset_alloc_model_0.asset_class IS 'Asset Allocation Class; from asset class Meta Data types';

COMMENT ON COLUMN p_i_asset_alloc_model_0.asset_class_strat IS 'what product does this hold (from table of products) or a cusip if its not a SMA/ETF/MF available for that program

One asset class can have multipe stategies. eg Equity can have multiple equity holdings';

COMMENT ON COLUMN p_i_asset_alloc_model_0.strat_pct IS 'percentage of that strategy. Total asset allocation model totals to a 100%';

COMMENT ON COLUMN p_i_asset_alloc_model_0.model_status IS '0 - TERMINATED
1 - ACTIVE
2 - ON HOLD';

COMMENT ON COLUMN p_i_asset_alloc_model_0.active_date IS 'Date this model was or will be activated';

COMMENT ON COLUMN p_i_asset_alloc_model_0.model_type IS '0 - new money
1 - existing accounts';

COMMENT ON COLUMN p_i_asset_alloc_model_0.prog_id IS 'what program is this allocation available in?';

COMMENT ON TABLE p_i_product_prog IS 'Product available for selection in  a certain program when building out the asset allocation';

COMMENT ON COLUMN p_i_product_prog.prog_id IS 'Program ID; foreign key';

COMMENT ON COLUMN p_i_product_prog.product_id IS 'products available in a program; 

1 to N relationship: program -> strategy';

COMMENT ON COLUMN p_i_product_prog.product_status IS 'Status of a specific product in an program

0 - PENDING ACTIVE
1 - INVEST
2 - MAINTAIN
3 - TERMINATED';

COMMENT ON COLUMN p_i_product_prog.status_date IS 'date for this status';

COMMENT ON COLUMN p_i_product_prog.prod_fee IS 'product';

COMMENT ON TABLE p_l_loan_products IS 'Lending Domain:

generic loan model';

COMMENT ON COLUMN p_l_loan_products.loan_type IS 'student, auto, cc, sbl, personal, loc, mortgage, other';

COMMENT ON COLUMN p_l_loan_products.can_deduct_tax IS '0 for NO, 1 for YES';

COMMENT ON COLUMN p_l_loan_products.penalty_prepay IS '0 for NO, 1 for YES';

COMMENT ON COLUMN p_l_loan_products.first_coupon_change IS 'change in # of days

30
60
90';

COMMENT ON COLUMN p_l_loan_products.tot_default_exposure IS 'total exposure across all loans';

COMMENT ON COLUMN p_l_loan_products.total_loan_disbursed IS 'if HELOC';

COMMENT ON COLUMN p_l_loan_products.prepay_penalty IS '0 for NO, 1 for YES';

COMMENT ON COLUMN p_l_loan_products.note_type IS 'revolving credit
fixed term loan
letter of credit';

COMMENT ON COLUMN p_l_loan_products.index_code IS 'libor 30 etc';

