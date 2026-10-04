---
id: software.seguranca.tranche14.001399
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

# Proteção Contra Força Bruta em Hardware (**Dictionary Attack Lockout**: `tpm2_dictionarylockout`), Senhas de Hierarquia (`tpm2_changeauth`) e **TRNG (`tpm2_getrandom`)**

## Em uma frase
Por que um PIN numérico de 6 dígitos protegendo uma chave dentro do **TPM 2.0** é imensamente mais resistente a ataques de força bruta do que um PIN de 6 dígitos protegendo um arquivo comum no disco rígido?

## Por que importa
Porque um arquivo no disco pode ser copiado para um cluster de GPUs que testa 10 bilhões de PINs por segundo offline, enquanto uma chave dentro do TPM 2.0 só pode ser testada enviando comandos para o próprio chip físico, que possui proteção de hardware chamada **Dictionary Attack (DA) Lockout (`tpm2_dictionarylockout`)**!

## Como funciona
O mecanismo de **Dictionary Attack Lockout** do TPM 2.0 monitora um contador não-volátil de falhas de autenticação (`TPM_PT_LOCKOUT_COUNTER`): por exemplo, após **`max-tries = 5`** tentativas incorretas de PIN/senha em objetos protegidos por `userwithauth`, o chip TPM entra em **estado de bloqueio (`Lockout`) por `recovery-time = 1800` segundos (30 minutos)** para cada tentativa extra, tornando matematicamente inviável adivinhar o PIN por força bruta!

## Exemplo
```bash
# Inspecionar os contadores atuais de Dictionary Attack Lockout do TPM, configurar os limites (max-tries=5) e extrair 32 bytes do TRNG de hardware
tpm2_getcap properties-variable | grep -E "TPM2_PT_(LOCKOUT|MAX_AUTH_FAIL)"
tpm2_dictionarylockout --setup-parameters --max-tries=5 --recovery-time=1800 --lockout-recovery-time=3600
tpm2_getrandom --hex 32
```

## Limites e trade-offs
Veja na última linha do exemplo acima outro recurso valioso do chip TPM 2.0: o **Gerador de Números Aleatórios Verdadeiros em Hardware (`TRNG` — `tpm2_getrandom`)**, baseado em fontes físicas de entropia térmica/ruído dentro do criptoprocessador! Você pode usar `tpm2_getrandom` (ou o driver `tpm-rng` do Kernel Linux em `/dev/hwrng`) para alimentar o pool de entropia do kernel logo no primeiro milissegundo do boot ou para gerar chaves criptográficas de alta entropia!

## Como verificar
Em servidores de produção, defina senhas administrativas fortes para as hierarquias `owner`, `endorsement` e `lockout` usando **`tpm2_changeauth -c o`**, **`tpm2_changeauth -c e`** e **`tpm2_changeauth -c l`** para impedir que processos não autorizados alterem parâmetros de lockout ou criem chaves persistentes sem autorização.

## Conexões
- [[tpm2-nvram-armazenamento-seguro-contadores-monotonicos-anti-rollback]] — Veja também: Memória Não-Volátil (**NVRAM**: `tpm2_nvdefine`, `tpm2_nvwrite`, `tpm2_nvread`) e **Contadores Monotônicos Anti-Rollback (`tpm2_nvincrement`)** no TPM 2.0.
- [[tpm2-simulacao-testes-ci-cd-swtpm-tcti-qemu-vtpm-containers]] — Veja também: Testes Automatizados em CI/CD e Virtualização (**`vTPM`**) com **`swtpm` (`libtpms`)** e Seleção de **`TCTI` (`TPM2TOOLS_TCTI`)** no `tpm2-tss`.
- [[tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs]] — Referência cruzada direta com tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs.
- [[tpm2-politicas-avancadas-ea-policyauthorize-policysigned-policyor-pin]] — Referência cruzada direta com tpm2-politicas-avancadas-ea-policyauthorize-policysigned-policyor-pin.

## Fontes
- [Official `tpm2-tools` GitHub Repository (`tpm2-software/tpm2-tools`)](https://raw.githubusercontent.com/tpm2-software/tpm2-tools/master/README.md) — repositório oficial dos utilitários `tpm2-tools` cobrindo criação de chaves, selagem em PCRs, políticas EA, cotações de atestação remota (`tpm2_quote`), NVRAM e Dictionary Attack Lockout; consultado em 2026-10-03.
- [Official TCG TPM2 Software Stack (`tpm2-software/tpm2-tss`) GitHub Repository](https://raw.githubusercontent.com/tpm2-software/tpm2-tss/master/README.md) — documentação oficial da pilha `tpm2-tss` detalhando as camadas arquiteturais `libtss2-fapi`, `libtss2-esys`, `libtss2-sys`, `libtss2-mu` e módulos `TCTI` (`device`, `swtpm`, `mssim`, `tctildr`); consultado em 2026-10-03.
