---
id: software.seguranca.tranche14.001395
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/tpm2-software/tpm2-tools/master/README.md", "https://raw.githubusercontent.com/tpm2-software/tpm2-tss/master/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Políticas Avançadas de Autorização (**Enhanced Authorization — EA**) no TPM 2.0: **`tpm2_policyauthorize` (Políticas Assinadas)**, **`tpm2_policyor`** e **`tpm2_policysecret`**

## Em uma frase
Se você selar um segredo diretamente nos hashes brutos dos PCRs `0, 4, 7, 8, 9` (conhecido como *Brittle PCR Policy*), toda vez que a sua equipe aplicar uma atualização de segurança do Kernel Linux ou do firmware UEFI, o hash do novo kernel mudará e será necessário re-selar o segredo localmente em cada máquina! Como o **TPM 2.0** resolve esse problema em frotas corporativas de milhares de servidores?

## Por que importa
Com o mecanismo de **Enhanced Authorization (`EA`)** do TPM 2.0, especificamente o comando **`TPM2_PolicyAuthorize` (`tpm2_policyauthorize`)**!

## Como funciona
Em vez de prender o objeto selado a um hash fixo e imutável de PCR, você prende o objeto à **Chave Pública de uma Autoridade de Políticas da sua empresa (`Policy Signing Key`)**! Sempre que a sua equipe de Engenharia compila e aprova um novo Kernel Linux no CI/CD, o pipeline assina digitalmente os novos valores esperados de PCR para aquele kernel (`openssl dgst -sha256 -sign policy_ca.key`). No boot, o servidor apresenta os PCRs atuais + a assinatura da sua equipe: o chip TPM verifica a assinatura com `tpm2_verifysignature` + `tpm2_policyauthorize` e **destrava o segredo para qualquer versão de Kernel assinada pela empresa sem nunca precisar re-selar o objeto**!

## Exemplo
```bash
# Iniciar uma sessao de politica de teste (trial session) no TPM 2.0 combinando PCR + exigencia de senha/PIN (policyauthvalue)
tpm2_startauthsession -S session.ctx
tpm2_policypcr -S session.ctx -l sha256:0,7
tpm2_policyauthvalue -S session.ctx
tpm2_getpolicydigest -S session.ctx -o policy_pcr_e_pin.digest
tpm2_flushcontext session.ctx
```

## Limites e trade-offs
Veja como a combinação **`tpm2_policypcr` + `tpm2_policyauthvalue` (`TPM + PIN`)** mostrada acima é uma defesa intransponível contra ataques físicos de bancada (*Cold Boot* ou *TPM Bus Sniffing* em chips TPM discretos no barramento SPI/LPC): mesmo que o computador dê boot com o sistema operacional intacto (`PCR 0,7` corretos), o TPM **ainda exige que o operador digite o PIN (`authValue`)**, cujo contador de falhas é protegido em hardware pelo **Dictionary Attack Lockout** do TPM!

## Como verificar
Já o comando **`tpm2_policyor`** permite criar ramificações lógicas `OU` (por exemplo: *"Desbloqueie o segredo SE (os PCRs de produção baterem) OU SE (um administrador apresentar uma assinatura criptográfica de recuperação de emergência via `tpm2_policysigned`)"*).

## Conexões
- [[tpm2-selagem-segredos-sealing-unsealing-pcr-policy-luks-systemd-cryptenroll]] — Veja também: Selagem de Segredos (**Sealing / Unsealing** Vinculado a **PCRs**) com `tpm2_createpolicy`, `tpm2_unseal` e Desbloqueio **LUKS2 (`systemd-cryptenroll`)**.
- [[tpm2-atestacao-remota-ak-ek-tpm2-quote-checkquote-verificacao]] — Veja também: Atestação Remota de Hardware e Boot (**Remote Attestation**) no TPM 2.0: **Endorsement Key (`EK`)**, **Attestation Key (`AK`)**, **`tpm2_quote`** e **`tpm2_checkquote`**.
- [[tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs]] — Referência cruzada direta com tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs.
- [[tpm2-nvram-armazenamento-seguro-contadores-monotonicos-anti-rollback]] — Referência cruzada direta com tpm2-nvram-armazenamento-seguro-contadores-monotonicos-anti-rollback.

## Fontes
- [Official `tpm2-tools` GitHub Repository (`tpm2-software/tpm2-tools`)](https://raw.githubusercontent.com/tpm2-software/tpm2-tools/master/README.md) — repositório oficial dos utilitários `tpm2-tools` cobrindo criação de chaves, selagem em PCRs, políticas EA, cotações de atestação remota (`tpm2_quote`), NVRAM e Dictionary Attack Lockout; consultado em 2026-10-03.
- [Official TCG TPM2 Software Stack (`tpm2-software/tpm2-tss`) GitHub Repository](https://raw.githubusercontent.com/tpm2-software/tpm2-tss/master/README.md) — documentação oficial da pilha `tpm2-tss` detalhando as camadas arquiteturais `libtss2-fapi`, `libtss2-esys`, `libtss2-sys`, `libtss2-mu` e módulos `TCTI` (`device`, `swtpm`, `mssim`, `tctildr`); consultado em 2026-10-03.
