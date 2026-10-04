---
id: software.seguranca.tranche08.000735
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

# Clevis + LUKS2 (`clevis luks bind`): Desbloqueio Automatizado da Partição Raiz (`/`) no Boot via **`dracut` / `initramfs-tools`** e Rede Pré-Boot

## Em uma frase
O comando **`clevis luks bind -d <dispositivo> <pin> '<config_json>'`** gera automaticamente uma nova passphrase de alta entropia, adiciona-a em um Keyslot livre do volume LUKS1/LUKS2 (via `luksmeta` no LUKS1 ou como um **Token nativo `clevis`** no cabeçalho JSON do LUKS2) e cifra essa passphrase usando o Pin Clevis especificado.

## Por que importa
Para que a partição raiz (`/`) criptografada de um servidor Linux desbloqueie sozinha no boot sem intervenção humana, os pacotes **`clevis-dracut`** (RHEL/Fedora/Alma/Rocky) ou **`clevis-initramfs`** (Debian/Ubuntu) + **`clevis-systemd`** injetam o cliente Clevis e a pilha de rede dentro da imagem **`initramfs`**.

## Como funciona
Durante o boot inicial (*initrd*), antes de montar `/`, o `initramfs` sobe a interface de rede (via DHCP ou IP estático configurado na linha de comando do kernel GRUB `rd.neednet=1 ip=...`), contata o servidor Tang para decifrar o JWE do token LUKS2 e destrava o volume raiz automaticamente!

## Exemplo
```bash
# Vincular uma particao LUKS2 a uma politica Clevis (Tang) e atualizar a imagem initramfs para desbloqueio no boot
sudo clevis luks bind -d /dev/nvme0n1p3 tang '{"url":"http://tang01.dc.internal.corp","thp":"kWwirxc5PhkFIH0yE28nc-EvjDY"}' -y
sudo clevis luks list -d /dev/nvme0n1p3
```

## Limites e trade-offs
Conforme documentado no `README.md` oficial do Clevis, em sistemas baseados em `dracut` (RHEL/Fedora) que usam um Pin de rede (`tang`), garanta que a rede seja ativada no initramfs (`dracut -f --regenerate-all` com `rd.neednet=1`), e em sistemas Debian/Ubuntu adicione `_netdev` (ou `initramfs` para volumes `/var` separados) em `/etc/crypttab` seguido de `sudo update-initramfs -u -k all`.

## Como verificar
Nunca remova a passphrase de emergência humana (Keyslot 0) ao vincular o Clevis (que ocupará ex.: o Keyslot 1): se a rede do datacenter estiver desligada, o console físico continuará aceitando a senha de emergência.

## Conexões
- [[clevis-politicas-quorum-shamir-secret-sharing-sss-tang-tpm2]] — Veja também: Clevis Pin **`sss` (*Shamir's Secret Sharing*)**: Políticas de Quórum de Alta Disponibilidade (`t: 2` de 3 Tangs) e Vinculação Híbrida **`TPM2` + `Tang`**.
- [[clevis-auditoria-regeneracao-clevis-luks-list-regen-unbind-edit]] — Veja também: Clevis: Ciclo de Vida de Vínculos LUKS (`clevis luks list`, `unlock`, `regen`, `edit` e `unbind`) após Rotação de Chaves Tang ou Mudança de PCRs.
- [[clevis-arquitetura-nbde-tang-mccallum-relyea-ecmr-sem-escrow]] — Referência cruzada direta com clevis-arquitetura-nbde-tang-mccallum-relyea-ecmr-sem-escrow.
- [[cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey]] — Referência cruzada direta com cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey.

## Fontes
- [Clevis Official GitHub — Automated Decryption Framework & Pins (tang, tpm2, sss, pkcs11)](https://raw.githubusercontent.com/latchset/clevis/master/README.md) — documentação oficial do framework Clevis cobrindo pins tang, tpm2, sss (Shamir Secret Sharing), pkcs11 e integração LUKS2/initramfs; consultado em 2026-10-03.
- [Tang Official GitHub — Stateless Network-Bound Cryptographic Server & ECMR Protocol](https://raw.githubusercontent.com/latchset/tang/master/README.md) — documentação oficial do servidor Tang cobrindo protocolo McCallum-Relyea (ECMR), geração/rotação de chaves JWK e operação stateless; consultado em 2026-10-03.
- [Latchset JOSE Official C Library & CLI Reference](https://github.com/latchset/jose) — repositório oficial da biblioteca e utilitário jose para objetos JWE/JWK/JWS utilizados pelo Clevis e Tang; consultado em 2026-10-03.
