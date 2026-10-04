---
id: software.seguranca.tranche14.001393
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

# Gerenciamento de Chaves no TPM 2.0: **`tpm2_createprimary`**, **`tpm2_create`**, **`tpm2_load`** e Persistência em NVRAM com **`tpm2_evictcontrol`**

## Em uma frase
Por que quando você executa **`tpm2_createprimary -C o -c primary.ctx`**, o comando leva alguns milissegundos e **sempre gera exatamente a mesma chave primária (`Storage Root Key — SRK`)**, mesmo que você apague o arquivo `primary.ctx` e reinicie o computador?

## Por que importa
Porque cada hierarquia do TPM (`Owner -C o`, `Endorsement -C e`, `Platform -C p`) possui uma **Semente Primária Secreta (`Primary Seed`)** gravada permanentemente dentro do silício do TPM! O comando `tpm2_createprimary` usa um KDF determinístico interno do hardware sobre essa semente + o template do algoritmo (`-G ecc256` ou `-G rsa2048`): assim, a Chave Primária atua como uma **Chave Mestra KEK (*Key Encryption Key*) interna do chip** que envolve (*wraps*) todas as chaves filhas!

## Como funciona
Quando você cria uma chave filha com **`tpm2_create -C primary.ctx -G ecc -u key.pub -r key.priv`**, o arquivo `key.priv` salvo no disco **NÃO é uma chave privada em texto claro**: ele é um blob cifrado pela chave primária do TPM que **só pode ser decifrado e carregado dentro daquele exato chip TPM (`tpm2_load`)**!

## Exemplo
```bash
# Criar uma chave primaria ECC P-256 na hierarquia Owner (-C o), gerar uma chave filha de assinatura ECDSA, carrega-la no TPM e assinar um arquivo
tpm2_createprimary -C o -g sha256 -G ecc -c primary.ctx
tpm2_create -C primary.ctx -g sha256 -G ecc:ecdsa-sha256:null -u app_sign.pub -r app_sign.priv
tpm2_load -C primary.ctx -u app_sign.pub -r app_sign.priv -c app_sign.ctx
echo "Mensagem Critica Auditar" > msg.txt
tpm2_sign -c app_sign.ctx -g sha256 -o msg.sig msg.txt
tpm2_verifysignature -c app_sign.ctx -g sha256 -m msg.txt -s msg.sig
```

## Limites e trade-offs
E se você não quiser manter os arquivos `.ctx` / `.priv` no sistema de arquivos e preferir que uma chave primária (como a **SRK** no endereço padrão TCG `0x81000001`) ou uma chave de aplicação fique **gravada permanentemente dentro da memória não-volátil (NVRAM) do próprio chip TPM** através de reboots? Basta usar **`tpm2_evictcontrol -C o -c primary.ctx 0x81000001`** (e `tpm2_getcap handles-persistent` para listar todos os handles persistidos no chip)!

## Como verificar
Note os atributos de segurança padrão de toda chave gerada pelo `tpm2_create`: **`fixedtpm`** e **`fixedparent`** — que garantem criptograficamente que aquela chave jamais poderá ser migrada ou exportada para outro chip TPM!

## Conexões
- [[tpm2-registradores-pcr-measured-boot-extend-sha256-uefi-eventlog]] — Veja também: Funcionamento dos **PCRs (*Platform Configuration Registers*)** e **Measured Boot** no TPM 2.0: A Operação Unidirecional **`PCR_Extend`** e os Bancos **`sha256`**.
- [[tpm2-selagem-segredos-sealing-unsealing-pcr-policy-luks-systemd-cryptenroll]] — Veja também: Selagem de Segredos (**Sealing / Unsealing** Vinculado a **PCRs**) com `tpm2_createpolicy`, `tpm2_unseal` e Desbloqueio **LUKS2 (`systemd-cryptenroll`)**.
- [[tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs]] — Referência cruzada direta com tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs.
- [[tpm2-pkcs11-ssh-tls-nginx-openvpn-chaves-hardware-nao-exportaveis]] — Referência cruzada direta com tpm2-pkcs11-ssh-tls-nginx-openvpn-chaves-hardware-nao-exportaveis.

## Fontes
- [Official `tpm2-tools` GitHub Repository (`tpm2-software/tpm2-tools`)](https://raw.githubusercontent.com/tpm2-software/tpm2-tools/master/README.md) — repositório oficial dos utilitários `tpm2-tools` cobrindo criação de chaves, selagem em PCRs, políticas EA, cotações de atestação remota (`tpm2_quote`), NVRAM e Dictionary Attack Lockout; consultado em 2026-10-03.
- [Official TCG TPM2 Software Stack (`tpm2-software/tpm2-tss`) GitHub Repository](https://raw.githubusercontent.com/tpm2-software/tpm2-tss/master/README.md) — documentação oficial da pilha `tpm2-tss` detalhando as camadas arquiteturais `libtss2-fapi`, `libtss2-esys`, `libtss2-sys`, `libtss2-mu` e módulos `TCTI` (`device`, `swtpm`, `mssim`, `tctildr`); consultado em 2026-10-03.
