---
id: software.seguranca.tranche15.001411
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

# Arquitetura do **CNCF Keylime (`keylime/keylime` & `rust-keylime`)**: Atestação Remota Contínua Baseada em **TPM 2.0**, `Verifier`, `Registrar`, `Tenant` e Agente Oficial em **Rust**

## Em uma frase
Imagine que você gerencia servidores bare-metal em colocation, nós de **Edge Computing / 5G / IoT** instalados em torres remotas sem vigilância física, ou máquinas em nuvem híbrida. Como garantir continuamente — a cada 2 segundos — que **nenhum invasor trocou o bootloader, adulterou o Kernel Linux ou executou um binário trojanizado em memória**, e só entregar chaves criptográficas para a máquina **depois** de provar criptograficamente no chip **TPM 2.0** que o sistema está 100% íntegro?

## Por que importa
Com o **CNCF Keylime (`keylime/keylime`)**, o sistema open-source de confiança escalável e atestação remota contínua ancorado em hardware **TPM 2.0**!

## Como funciona
A arquitetura do Keylime é composta por **4 componentes**: **(1) `Keylime Agent` (`rust-keylime`)** — o agente oficial escrito em **Rust memory-safe** que roda na máquina monitorada e se comunica diretamente com o chip `/dev/tpmrm0` via `libtss2-esys`; **(2) `Keylime Registrar`** — o banco de dados HTTPS que armazena as chaves públicas `EK` (*Endorsement Key*) e `AK` (*Attestation Key*) de todos os agentes e valida os certificados dos fabricantes de TPM; **(3) `Keylime Verifier`** — o motor central que solicita e verifica periodicamente as cotações (`TPM2_Quote`), o log de *Measured Boot* UEFI e a lista de execução do **Linux IMA**; e **(4) `keylime_tenant`** — a CLI/API de comando e provisionamento!

## Exemplo
```bash
# Verificar o status dos servicos do plano de controle (keylime_registrar e keylime_verifier) e do agente oficial em Rust (keylime_agent)
systemctl status keylime_registrar keylime_verifier keylime_agent
keylime_tenant -c reglist
```

## Limites e trade-offs
Conforme destacado na documentação oficial do Keylime e do `rust-keylime`: **o agente reescrito em Rust (`rust-keylime`) é o agente oficial de produção** (substituindo o antigo agente em Python, depreciado e removido no Keylime 7.0+), pois o agente roda na máquina alvo com acesso ao TPM e requer máxima segurança de memória e baixo footprint de CPU/RAM!

## Como verificar
E atenção ao aviso de segurança enfático do `README.md` do Keylime: embora o Keylime funcione com emuladores `swtpm` para testes de CI/CD e desenvolvimento, **JAMAIS use um emulador de TPM em software em produção**, pois apenas um chip **TPM 2.0 físico de hardware** oferece uma Raiz de Confiança isolada contra comprometimento do sistema operacional!

## Conexões
- [[keylime-fluxo-registro-ek-ak-makecredential-activatecredential-ekcert]] — Veja também: Bootstrapping de Confiança no Keylime: Validação da **Endorsement Key (`EKCert`)**, Desafio **`MakeCredential` / `ActivateCredential`** e Registro da **`AK`** no `Registrar`.
- [[keylime-monitoramento-integridade-runtime-linux-ima-allowlists-polices]] — Referência cruzada direta com keylime-monitoramento-integridade-runtime-linux-ima-allowlists-polices.
- [[tpm2-atestacao-remota-ak-ek-tpm2-quote-checkquote-verificacao]] — Referência cruzada direta com tpm2-atestacao-remota-ak-ek-tpm2-quote-checkquote-verificacao.

## Fontes
- [CNCF Keylime Official GitHub Repository (`keylime/keylime`)](https://raw.githubusercontent.com/keylime/keylime/master/README.md) — repositório oficial do projeto CNCF Keylime cobrindo arquitetura de atestação remota TPM 2.0, Verifier, Registrar, Tenant, Measured Boot, IMA e Encrypted Payloads; consultado em 2026-10-03.
- [Keylime Official Rust Agent Repository (`keylime/rust-keylime`)](https://raw.githubusercontent.com/keylime/rust-keylime/master/README.md) — documentação oficial do agente `rust-keylime` em Rust sobre `rust-tss-esapi` detalhando configuração `/etc/keylime/agent.conf`, mTLS e revogação local; consultado em 2026-10-03.
