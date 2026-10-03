---
id: software.seguranca.tranche08.000734
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

# Clevis Pin **`sss` (*Shamir's Secret Sharing*)**: Políticas de Quórum de Alta Disponibilidade (`t: 2` de 3 Tangs) e Vinculação Híbrida **`TPM2` + `Tang`**

## Em uma frase
O Pin mais poderoso do Clevis para arquiteturas corporativas resilientes e de alta segurança é o **`sss` (*Shamir's Secret Sharing*)**: ele divide a chave de decriptação em $N$ fragmentos criptográficos (cada um protegido por um Pin filho diferente) e exige um limiar (**threshold `"t"`**) de fragmentos válidos para reconstruir o segredo.

## Por que importa
Isso resolve dois cenários arquiteturais opostos dependendo do valor de `"t"`: **(1) Alta Disponibilidade de Rede (`"t": 1` ou `"t": 2` entre 3 servidores Tang em racks diferentes)**: se `"t": 1` (ou `"t": 2` de `3`), o servidor de produção continua dando boot automaticamente mesmo que um servidor Tang esteja em manutenção!

## Como funciona
E **(2) Defesa contra Roubo Físico de Servidor com TPM2 (`"t": 2` combinando `tpm2` + `tang`)**: se um servidor tiver apenas TPM2, um ladrão que roube o servidor físico inteiro do rack leva junto a placa-mãe com o chip TPM2; se tiver apenas Tang, qualquer máquina na VLAN alcança o Tang; mas com **`sss` exigindo `"t": 2` onde um pino é `tpm2` (hardware da placa-mãe) e o outro pino é `tang` (presença física na VLAN do datacenter)**, o disco só desbloqueia se for **aquele hardware exato E estiver dentro da rede do datacenter**!

## Exemplo
```bash
# Politica Shamir Secret Sharing (sss) exigindo SIMULTANEAMENTE (t: 2) o chip TPM 2.0 local (PCR 7) E o servidor Tang da rede!
clevis encrypt sss '{
  "t": 2,
  "pins": {
    "tpm2": {"hash": "sha256", "key": "ecc", "pcr_bank": "sha256", "pcr_ids": "7"},
    "tang": {"url": "http://tang01.dc.internal.corp", "thp": "kWwirxc5PhkFIH0yE28nc-EvjDY"}
  }
}' -y < /etc/secops/master.secret > /etc/secops/master.secret.jwe
```

## Limites e trade-offs
Você pode aninhar um Pin `sss` dentro de outro Pin `sss`! Por exemplo: no nível superior `"t": 2` exigindo (`tpm2` **E** um sub-pino `sss` com `"t": 1` contendo `[tang01, tang02]`), garantindo **TPM2 obrigatório + alta disponibilidade entre dois servidores Tang**!

## Como verificar
Valide a política `sss` aninhada com `clevis decrypt` e teste desligar `tang01` para confirmar o failover transparente para `tang02`.

## Conexões
- [[clevis-criptografia-dados-pins-tang-tpm2-pkcs11-jwe-formato]] — Veja também: Clevis: Arquitetura de **Pins (`tang`, `tpm2`, `sss`, `pkcs11`)** e Criptografia de Segredos em Objetos **JWE (`clevis encrypt` / `clevis decrypt`)**.
- [[clevis-integracao-luks2-clevis-luks-bind-initramfs-dracut-systemd]] — Veja também: Clevis + LUKS2 (`clevis luks bind`): Desbloqueio Automatizado da Partição Raiz (`/`) no Boot via **`dracut` / `initramfs-tools`** e Rede Pré-Boot.
- [[clevis-arquitetura-nbde-tang-mccallum-relyea-ecmr-sem-escrow]] — Referência cruzada direta com clevis-arquitetura-nbde-tang-mccallum-relyea-ecmr-sem-escrow.

## Fontes
- [Clevis Official GitHub — Automated Decryption Framework & Pins (tang, tpm2, sss, pkcs11)](https://raw.githubusercontent.com/latchset/clevis/master/README.md) — documentação oficial do framework Clevis cobrindo pins tang, tpm2, sss (Shamir Secret Sharing), pkcs11 e integração LUKS2/initramfs; consultado em 2026-10-03.
- [Tang Official GitHub — Stateless Network-Bound Cryptographic Server & ECMR Protocol](https://raw.githubusercontent.com/latchset/tang/master/README.md) — documentação oficial do servidor Tang cobrindo protocolo McCallum-Relyea (ECMR), geração/rotação de chaves JWK e operação stateless; consultado em 2026-10-03.
- [Latchset JOSE Official C Library & CLI Reference](https://github.com/latchset/jose) — repositório oficial da biblioteca e utilitário jose para objetos JWE/JWK/JWS utilizados pelo Clevis e Tang; consultado em 2026-10-03.
