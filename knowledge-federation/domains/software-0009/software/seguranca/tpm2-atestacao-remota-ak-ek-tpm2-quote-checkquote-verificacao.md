---
id: software.seguranca.tranche14.001396
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

# Atestação Remota de Hardware e Boot (**Remote Attestation**) no TPM 2.0: **Endorsement Key (`EK`)**, **Attestation Key (`AK`)**, **`tpm2_quote`** e **`tpm2_checkquote`**

## Em uma frase
Quando um servidor remoto ou dispositivo de borda (Edge/IoT) tenta se conectar à sua rede Zero-Trust (ou ingressar em um cluster Kubernetes / Teleport / Keylime), como o servidor central de verificação pode ter **certeza criptográfica à prova de falsificação** de que: **(1)** Aquela máquina é o hardware físico verdadeiro (e não uma VM clonada pelo invasor) e **(2)** O Kernel e o Secure Boot daquela máquina não foram adulterados?

## Por que importa
Através do protocolo de **Atestação Remota (`TPM 2.0 Remote Attestation`)** usando **`tpm2_createek`**, **`tpm2_createak`**, **`tpm2_quote`** e **`tpm2_checkquote`**!

## Como funciona
Por que usamos duas chaves (**`EK` + `AK`**)? A **Endorsement Key (`EK`)** é a chave de identidade única do chip (cujo certificado X.509 vem assinado de fábrica pela Intel, AMD, Infineon, Nuvoton ou STMicroelectronics!), mas a `EK` é uma chave de descriptografia restrita que não assina cotações diretamente. Por isso, cria-se uma **Attestation Key (`AK`, chave de assinatura restrita apenas a estruturas internas do TPM!)** vinculada criptograficamente à `EK` via `tpm2_makecredential` / `tpm2_activatecredential`. Em seguida, o Verificador envia um **`nonce` aleatório fresco**, o servidor executa **`tpm2_quote`** (que lê os PCRs internos do chip e os assina com a `AK` junto com o `nonce`), e o Verificador valida tudo offline com **`tpm2_checkquote`**!

## Exemplo
```bash
# Fluxo completo de Atestacao Remota TPM 2.0: gerar EK e AK, produzir uma cotacao assinada dos PCRs 0,4,7 com nonce (-q) e validar com tpm2_checkquote
tpm2_createek -c ek.ctx -G rsa -u ek.pub
tpm2_createak -C ek.ctx -c ak.ctx -G rsa -g sha256 -s rsassa -u ak.pub -n ak.name
NONCE="$(openssl rand -hex 16)"
tpm2_quote -c ak.ctx -l sha256:0,4,7 -q "$NONCE" -m quote.msg -s quote.sig -o quote.pcrs -g sha256
tpm2_checkquote -u ak.pub -m quote.msg -s quote.sig -f quote.pcrs -g sha256 -q "$NONCE"
```

## Limites e trade-offs
Por que uma chave comum de assinatura gerada fora do TPM (ou até uma chave não-restrita do TPM) **não poderia falsificar um `tpm2_quote`**? Porque a **Attestation Key (`AK`)** possui o atributo de hardware **`restricted`**: o chip TPM 2.0 se recusa fisicamente a usar uma chave `restricted` para assinar qualquer dado externo arbitrário que comece com o número mágico **`TPM_GENERATED_VALUE` (`0xff544347` = `\xffTCG`)**, que só o próprio firmware interno do TPM consegue colocar no cabeçalho de um `quote.msg`!

## Como verificar
Projetos open-source da CNCF como o **Keylime (`keylime/keylime`)** automatizam continuamente esse ciclo `tpm2_quote` + `IMA (Integrity Measurement Architecture)` do Kernel Linux para monitorar a integridade em tempo de execução de milhares de servidores!

## Conexões
- [[tpm2-politicas-avancadas-ea-policyauthorize-policysigned-policyor-pin]] — Veja também: Políticas Avançadas de Autorização (**Enhanced Authorization — EA**) no TPM 2.0: **`tpm2_policyauthorize` (Políticas Assinadas)**, **`tpm2_policyor`** e **`tpm2_policysecret`**.
- [[tpm2-pkcs11-ssh-tls-nginx-openvpn-chaves-hardware-nao-exportaveis]] — Veja também: Uso de Chaves TPM 2.0 Não-Exportáveis em **OpenSSH, Nginx, OpenVPN, StrongSwan e Rust/Go** com **`tpm2-pkcs11`** e **`tpm2-openssl` Provider**.
- [[tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs]] — Referência cruzada direta com tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs.
- [[tpm2-registradores-pcr-measured-boot-extend-sha256-uefi-eventlog]] — Referência cruzada direta com tpm2-registradores-pcr-measured-boot-extend-sha256-uefi-eventlog.
- [[teleport-ingresso-seguro-nos-join-tokens-cloud-iam-tpm-node-joining]] — Referência cruzada direta com teleport-ingresso-seguro-nos-join-tokens-cloud-iam-tpm-node-joining.

## Fontes
- [Official `tpm2-tools` GitHub Repository (`tpm2-software/tpm2-tools`)](https://raw.githubusercontent.com/tpm2-software/tpm2-tools/master/README.md) — repositório oficial dos utilitários `tpm2-tools` cobrindo criação de chaves, selagem em PCRs, políticas EA, cotações de atestação remota (`tpm2_quote`), NVRAM e Dictionary Attack Lockout; consultado em 2026-10-03.
- [Official TCG TPM2 Software Stack (`tpm2-software/tpm2-tss`) GitHub Repository](https://raw.githubusercontent.com/tpm2-software/tpm2-tss/master/README.md) — documentação oficial da pilha `tpm2-tss` detalhando as camadas arquiteturais `libtss2-fapi`, `libtss2-esys`, `libtss2-sys`, `libtss2-mu` e módulos `TCTI` (`device`, `swtpm`, `mssim`, `tctildr`); consultado em 2026-10-03.
