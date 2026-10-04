---
id: software.seguranca.tranche15.001413
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

# Entrega Segura de Segredos (**Encrypted Payload Provisioning**) no Keylime: Derivação Tripartida da Chave **`U` + `V` = `K`** só Após Aprovação na Atestação!

## Em uma frase
Muitas ferramentas de gerenciamento de configuração (Ansible, Cloud-Init) empurram segredos ou certificados para um servidor recém-instalado assim que o SSH responde — sem verificar se a BIOS ou o Kernel daquela máquina foram comprometidos! Como o **Keylime** entrega um **Payload Criptografado (`-f filetosend` ou `--cert` Autoridade Certificadora)** garantindo que **nem mesmo o `Verifier` sozinho nem um sniffer na rede consigam decifrar o segredo se o TPM falhar na atestação**?

## Por que importa
O Keylime utiliza um protocolo genial de **Divisão Criptográfica de Chave (`Split-Key Secret Sharing: K = U XOR V`)** entre o **`Tenant`**, o **`Verifier`** e o **`Agent`**!

## Como funciona
Funciona assim: **(1)** Quando você roda `keylime_tenant -c add ... -f segredo.tar.gz`, o `Tenant` gera uma chave simétrica aleatória `K` (AES-GCM), cifra o payload com `K` e divide `K` em duas metades criptográficas: **`U`** e **`V`** (`K = U XOR V`); **(2)** O `Tenant` envia a metade `U` (envolvida pela chave pública do TPM do agente) e o payload cifrado para o `Agent`, e envia a outra metade **`V`** para o `Verifier` via mTLS; **(3) O `Agent` ainda NÃO consegue decifrar o payload porque só tem `U`!**; e **(4)** O `Verifier` solicita uma cotação **`TPM2_Quote`** ao `Agent`: **somente SE todos os PCRs de boot e o log IMA passarem 100% na validação**, o `Verifier` libera a metade **`V`** para o `Agent`, que reconstrói `K = U XOR V` em memória (`tmpfs` `/var/lib/keylime/secure`) e executa o script `autorun.sh`!

## Exemplo
```bash
# Provisionar um agente Keylime enviando um payload criptografado (--include) que so sera decifrado na memoria apos a atestacao do TPM 2.0 passar
keylime_tenant -c add \
  -t 10.20.30.15 \
  -v 10.20.30.10 \
  -u d432fbb3-d2f1-4a97-9ef7-75bd81c00000 \
  --include ./pacote_chaves_producao/ \
  --tpm_policy '{"7": "094524..."}'
```

## Limites e trade-offs
Onde o `keylime_agent` monta e decifra esse payload em memória no servidor Linux para garantir que os segredos **jamais toquem o disco físico (SSD/HDD)**? Em uma partição **`tmpfs` em RAM (`/var/lib/keylime/secure`)**: se alguém puxar o cabo de energia do servidor para roubar o disco, o conteúdo de `/var/lib/keylime/secure` desaparece instantaneamente!

## Como verificar
Além de enviar um arquivo ou diretório com `-f` / `--include`, você pode usar a flag **`--ca-dir`** no `keylime_tenant` para que o Keylime gere automaticamente um certificado X.509 mTLS de identidade do nó e o entregue dentro do payload cifrado!

## Conexões
- [[keylime-fluxo-registro-ek-ak-makecredential-activatecredential-ekcert]] — Veja também: Bootstrapping de Confiança no Keylime: Validação da **Endorsement Key (`EKCert`)**, Desafio **`MakeCredential` / `ActivateCredential`** e Registro da **`AK`** no `Registrar`.
- [[keylime-monitoramento-integridade-runtime-linux-ima-allowlists-polices]] — Veja também: Monitoramento de Integridade em Tempo de Execução (**Runtime Integrity Monitoring**) no Keylime com **Linux IMA (`Integrity Measurement Architecture` — `PCR 10`)**.
- [[keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent]] — Referência cruzada direta com keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent.
- [[tpm2-selagem-segredos-sealing-unsealing-pcr-policy-luks-systemd-cryptenroll]] — Referência cruzada direta com tpm2-selagem-segredos-sealing-unsealing-pcr-policy-luks-systemd-cryptenroll.

## Fontes
- [CNCF Keylime Official GitHub Repository (`keylime/keylime`)](https://raw.githubusercontent.com/keylime/keylime/master/README.md) — repositório oficial do projeto CNCF Keylime cobrindo arquitetura de atestação remota TPM 2.0, Verifier, Registrar, Tenant, Measured Boot, IMA e Encrypted Payloads; consultado em 2026-10-03.
- [Keylime Official Rust Agent Repository (`keylime/rust-keylime`)](https://raw.githubusercontent.com/keylime/rust-keylime/master/README.md) — documentação oficial do agente `rust-keylime` em Rust sobre `rust-tss-esapi` detalhando configuração `/etc/keylime/agent.conf`, mTLS e revogação local; consultado em 2026-10-03.
