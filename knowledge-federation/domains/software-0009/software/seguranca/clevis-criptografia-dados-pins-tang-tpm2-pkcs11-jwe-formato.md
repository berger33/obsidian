---
id: software.seguranca.tranche08.000733
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/latchset/clevis/master/README.md", "https://raw.githubusercontent.com/latchset/tang/master/README.md", "https://github.com/latchset/jose"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Clevis: Arquitetura de **Pins (`tang`, `tpm2`, `sss`, `pkcs11`)** e Criptografia de Segredos em Objetos **JWE (`clevis encrypt` / `clevis decrypt`)**

## Em uma frase
Na terminologia do Clevis, cada mecanismo de desbloqueio automatizado é implementado como um plugin chamado **Pin** (`clevis-encrypt-<pin>` e `clevis-decrypt-<pin>`), que recebe uma configuração JSON na criptografia e embute todos os metadados necessários dentro do próprio cabeçalho protegido do objeto **JWE (*JSON Web Encryption*, RFC 7516)**.

## Por que importa
Por isso, o comando **`clevis decrypt < segredo.jwe`** **não exige passar nenhum argumento de linha de comando nem arquivo de configuração**: o Clevis lê o cabeçalho do JWE (`clevis.pin`), descobre qual Pin foi usado (`tang`, `tpm2`, `sss` ou `pkcs11`) e invoca automaticamente o Pin correspondente para recuperar a chave e decifrar o payload!

## Como funciona
Além de desbloquear discos LUKS2, usar `clevis encrypt` / `clevis decrypt` diretamente sobre arquivos de configuração permite guardar segredos de bootstrap (como a chave de desbloqueio de um nó HashiCorp Vault ou chave privada de um agente) vinculados ao **TPM 2.0 + servidor Tang da rede interna**.

## Exemplo
```bash
# Criptografar um segredo vinculando-o ao servidor Tang (passando o thumbprint confiavel para execucao nao-interativa -y)
THP=$(curl -sf http://127.0.0.1/adv | jose fmt -j- -Og payload -y -o- | jose jwk use -i- -r -u verify -o- | jose jwk thp -i-)
echo "Segredo-De-Bootstrap-Do-No-2026" | clevis encrypt tang "{\"url\":\"http://127.0.0.1\",\"thp\":\"$THP\"}" -y > /tmp/bootstrap.jwe
clevis decrypt < /tmp/bootstrap.jwe
```

## Limites e trade-offs
Ao automatizar o provisionamento com Ansible/Terraform, sempre passe o **`"thp"`** (thumbprint da chave de assinatura do Tang obtido de forma confiável) ou o objeto **`"adv"`** no JSON do Pin `tang` junto com a flag **`-y`** para evitar TOFU cego na rede.

## Como verificar
Inspecione o cabeçalho protegido de um arquivo `.jwe` gerado pelo Clevis com `jose fmt -j /tmp/bootstrap.jwe -Og protected -y -o- | jq .`.

## Conexões
- [[clevis-operacao-servidor-tang-rotacao-chaves-jwk-adv-verificacao]] — Veja também: Tang Server: Operação de `/var/db/tang/`, Thumbprints **JWK (`S256`)** e **Rotação Graciosa de Chaves (`jose jwk gen`)** sem Quebrar o Boot.
- [[clevis-politicas-quorum-shamir-secret-sharing-sss-tang-tpm2]] — Veja também: Clevis Pin **`sss` (*Shamir's Secret Sharing*)**: Políticas de Quórum de Alta Disponibilidade (`t: 2` de 3 Tangs) e Vinculação Híbrida **`TPM2` + `Tang`**.
- [[clevis-arquitetura-nbde-tang-mccallum-relyea-ecmr-sem-escrow]] — Referência cruzada direta com clevis-arquitetura-nbde-tang-mccallum-relyea-ecmr-sem-escrow.
- [[cryptsetup-desbloqueio-hardware-systemd-cryptenroll-tpm2-fido2-pkcs11]] — Referência cruzada direta com cryptsetup-desbloqueio-hardware-systemd-cryptenroll-tpm2-fido2-pkcs11.

## Fontes
- [Clevis Official GitHub — Automated Decryption Framework & Pins (tang, tpm2, sss, pkcs11)](https://raw.githubusercontent.com/latchset/clevis/master/README.md) — documentação oficial do framework Clevis cobrindo pins tang, tpm2, sss (Shamir Secret Sharing), pkcs11 e integração LUKS2/initramfs; consultado em 2026-10-03.
- [Tang Official GitHub — Stateless Network-Bound Cryptographic Server & ECMR Protocol](https://raw.githubusercontent.com/latchset/tang/master/README.md) — documentação oficial do servidor Tang cobrindo protocolo McCallum-Relyea (ECMR), geração/rotação de chaves JWK e operação stateless; consultado em 2026-10-03.
- [Latchset JOSE Official C Library & CLI Reference](https://github.com/latchset/jose) — repositório oficial da biblioteca e utilitário jose para objetos JWE/JWK/JWS utilizados pelo Clevis e Tang; consultado em 2026-10-03.
