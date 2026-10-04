---
id: software.seguranca.tranche15.001412
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/keylime/keylime/master/README.md", "https://raw.githubusercontent.com/keylime/rust-keylime/master/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Bootstrapping de Confiança no Keylime: Validação da **Endorsement Key (`EKCert`)**, Desafio **`MakeCredential` / `ActivateCredential`** e Registro da **`AK`** no `Registrar`

## Em uma frase
Quando um novo servidor com `keylime_agent` liga pela primeira vez e se conecta ao **`keylime_registrar`**, como o Keylime tem certeza matemática de que está falando com um **chip físico TPM 2.0 autêntico** fabricado pela Infineon, Intel, AMD, Nuvoton ou STMicroelectronics — e não com um script malicioso do invasor fingindo ser um TPM e forjando chaves RSA/ECC em software?

## Por que importa
Através do protocolo criptográfico de **Validação de Certificado de Endosso (`EKCert`) + Desafio `TPM2_MakeCredential` / `TPM2_ActivateCredential`** do TCG!

## Como funciona
Veja a sequência exata executada entre o `keylime_agent` e o `keylime_registrar`: **(1)** O agente lê do chip TPM a chave pública de endosso (**`EK` — *Endorsement Key***), o certificado X.509 gravado de fábrica na NVRAM do TPM pelo fabricante do silício (**`EKCert`**) e gera uma chave de assinatura restrita (**`AK` — *Attestation Key***); **(2)** O `Registrar` verifica a assinatura do `EKCert` contra a **TPM Vendor CA Store** (as raízes oficiais dos fabricantes de chips TPM!); **(3)** Para provar que a `AK` realmente reside dentro do mesmo chip físico que possui aquela `EK`, o `Registrar` cifra um desafio secreto usando `MakeCredential(EK_pub, AK_name)`: **o chip TPM só consegue decifrar o desafio (`TPM2_ActivateCredential`) se a chave `AK` estiver carregada internamente naquele exato TPM dono da `EK`**!

## Exemplo
```bash
# Inspecionar no /etc/keylime/registrar.conf e verifier.conf a exigencia de validacao do certificado de fabrica do TPM (require_ek_cert)
grep -E "^(require_ek_cert|ek_check_script|tpm_cert_store)" /etc/keylime/registrar.conf /etc/keylime/verifier.conf || true
keylime_tenant -c regstatus -u d432fbb3-d2f1-4a97-9ef7-75bd81c00000
```

## Limites e trade-offs
Em servidores de produção com TPM 2.0 físico, mantenha sempre **`require_ek_cert = True`** e aponte **`tpm_cert_store = /var/lib/keylime/tpm_cert_store/`** para o diretório contendo os certificados intermediários e raízes dos fabricantes de TPM!

## Como verificar
E se a sua empresa adquiriu um lote de servidores cujo TPM não veio com `EKCert` pré-gravado na NVRAM ou utiliza `vTPM` assinado pela sua própria PKI interna? Você pode assinar as chaves `EK` com a CA interna da empresa e colocar o certificado da sua CA em `/var/lib/keylime/tpm_cert_store/` ou usar um script customizado em `ek_check_script`!

## Conexões
- [[keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent]] — Veja também: Arquitetura do **CNCF Keylime (`keylime/keylime` & `rust-keylime`)**: Atestação Remota Contínua Baseada em **TPM 2.0**, `Verifier`, `Registrar`, `Tenant` e Agente Oficial em **Rust**.
- [[keylime-provisionamento-payload-criptografado-bootstrap-chaves-mtls]] — Veja também: Entrega Segura de Segredos (**Encrypted Payload Provisioning**) no Keylime: Derivação Tripartida da Chave **`U` + `V` = `K`** só Após Aprovação na Atestação!.
- [[tpm2-atestacao-remota-ak-ek-tpm2-quote-checkquote-verificacao]] — Referência cruzada direta com tpm2-atestacao-remota-ak-ek-tpm2-quote-checkquote-verificacao.
- [[teleport-ingresso-seguro-nos-join-tokens-cloud-iam-tpm-node-joining]] — Referência cruzada direta com teleport-ingresso-seguro-nos-join-tokens-cloud-iam-tpm-node-joining.

## Fontes
- [CNCF Keylime Official GitHub Repository (`keylime/keylime`)](https://raw.githubusercontent.com/keylime/keylime/master/README.md) — repositório oficial do projeto CNCF Keylime cobrindo arquitetura de atestação remota TPM 2.0, Verifier, Registrar, Tenant, Measured Boot, IMA e Encrypted Payloads; consultado em 2026-10-03.
- [Keylime Official Rust Agent Repository (`keylime/rust-keylime`)](https://raw.githubusercontent.com/keylime/rust-keylime/master/README.md) — documentação oficial do agente `rust-keylime` em Rust sobre `rust-tss-esapi` detalhando configuração `/etc/keylime/agent.conf`, mTLS e revogação local; consultado em 2026-10-03.
