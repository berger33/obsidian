---
id: software.seguranca.tranche14.001391
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

# Arquitetura do **TPM 2.0 (`tpm2-tss` & `tpm2-tools`)**: Raiz de Confiança em Hardware, Camadas da Stack TCG (`FAPI`, `ESYS`, `TCTI`) e **As 4 Hierarquias (`Owner`, `Endorsement`, `Platform`, `Null`)**

## Em uma frase
O que é o chip **TPM 2.0 (*Trusted Platform Module 2.0*, especificação ISO/IEC 11889 do Trusted Computing Group — TCG)** presente em praticamente todos os servidores, notebooks corporativos e VMs modernas (`vTPM`), e como o Linux interage com ele através da stack oficial **`tpm2-tss` (`tpm2-software/tpm2-tss`)** e dos utilitários **`tpm2-tools`**?

## Por que importa
Diferente de armazenar chaves criptográficas em arquivos no disco (que qualquer malware ou atacante com acesso `root` pode copiar e exfiltrar!), o **TPM 2.0** é um criptoprocessador seguro isolado em hardware capaz de gerar chaves RSA/ECC internamente, **proibir por hardware que a chave privada jamais saia do chip**, medir a integridade de cada estágio do boot nos registradores **PCRs (*Platform Configuration Registers*)** e proteger contra força bruta via **Dictionary Attack Lockout**!

## Como funciona
No Linux, a stack oficial **`tpm2-tss`** é dividida nas camadas padronizadas pelo TCG: **`libtss2-fapi`** (*Feature API* de alto nível), **`libtss2-esys`** (*Enhanced System API* com gerenciamento de sessões e HMAC), **`libtss2-sys`** (*System API* 1:1 com comandos TPM), **`libtss2-mu`** (*Marshaling/Unmarshaling*) e **`libtss2-tcti`** (*TPM Command Transmission Interface*: `/dev/tpmrm0` com Resource Manager do kernel, `tpm2-abrmd`, `swtpm` ou `mssim`)!

## Exemplo
```bash
# Inspecionar as propriedades fixas do chip TPM 2.0 (fabricante, versao de firmware, algoritmos suportados) usando o Resource Manager /dev/tpmrm0
tpm2_getcap properties-fixed
tpm2_getcap algorithms
```

## Limites e trade-offs
Internamente, o TPM 2.0 organiza suas sementes criptográficas primárias em **4 Hierarquias independentes**: **(1) `Endorsement Hierarchy` (`-C e` / `TPM_RH_ENDORSEMENT`)** — ligada à identidade de fábrica do chip (**EK — *Endorsement Key***) para atestação de hardware genuíno; **(2) `Owner / Storage Hierarchy` (`-C o` / `TPM_RH_OWNER`)** — controlada pelo sistema operacional/usuário dono da máquina para proteger chaves e segredos (**SRK — *Storage Root Key***); **(3) `Platform Hierarchy` (`-C p`)** — controlada pelo firmware UEFI/BIOS; e **(4) `Null Hierarchy` (`-C n`)** — efêmera, cuja semente é destruída a cada reboot!

## Como verificar
No Linux moderno (Kernel 4.12+), sempre acesse o TPM através do dispositivo gerenciado pelo kernel **`/dev/tpmrm0`** (*In-Kernel Resource Manager*, usado automaticamente pelo `libtss2-tctildr`), que gerencia o swap da memória volátil limitada do TPM entre múltiplos processos concorrentes!

## Conexões
- [[tpm2-registradores-pcr-measured-boot-extend-sha256-uefi-eventlog]] — Veja também: Funcionamento dos **PCRs (*Platform Configuration Registers*)** e **Measured Boot** no TPM 2.0: A Operação Unidirecional **`PCR_Extend`** e os Bancos **`sha256`**.
- [[tpm2-hierarquia-chaves-createprimary-create-load-persist-evictcontrol]] — Referência cruzada direta com tpm2-hierarquia-chaves-createprimary-create-load-persist-evictcontrol.
- [[teleport-ingresso-seguro-nos-join-tokens-cloud-iam-tpm-node-joining]] — Referência cruzada direta com teleport-ingresso-seguro-nos-join-tokens-cloud-iam-tpm-node-joining.

## Fontes
- [Official `tpm2-tools` GitHub Repository (`tpm2-software/tpm2-tools`)](https://raw.githubusercontent.com/tpm2-software/tpm2-tools/master/README.md) — repositório oficial dos utilitários `tpm2-tools` cobrindo criação de chaves, selagem em PCRs, políticas EA, cotações de atestação remota (`tpm2_quote`), NVRAM e Dictionary Attack Lockout; consultado em 2026-10-03.
- [Official TCG TPM2 Software Stack (`tpm2-software/tpm2-tss`) GitHub Repository](https://raw.githubusercontent.com/tpm2-software/tpm2-tss/master/README.md) — documentação oficial da pilha `tpm2-tss` detalhando as camadas arquiteturais `libtss2-fapi`, `libtss2-esys`, `libtss2-sys`, `libtss2-mu` e módulos `TCTI` (`device`, `swtpm`, `mssim`, `tctildr`); consultado em 2026-10-03.
