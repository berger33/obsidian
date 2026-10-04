---
id: software.seguranca.tranche08.000736
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

# Clevis: Ciclo de Vida de Vínculos LUKS (`clevis luks list`, `unlock`, `regen`, `edit` e `unbind`) após Rotação de Chaves Tang ou Mudança de PCRs

## Em uma frase
Depois que frotas de servidores são vinculadas ao Clevis (`clevis luks bind`), a equipe de operações precisa auditar quais keyslots estão vinculados a quais servidores Tang/PCRs, atualizar os vínculos quando as chaves do servidor Tang são rotacionadas e remover vínculos antigos com segurança.

## Por que importa
Os subcomandos de ciclo de vida do `clevis luks` cobrem todas essas operações sem exigir digitar a senha mestre do disco: **`clevis luks list -d <dev>`** (mostra qual número de Keyslot LUKS está vinculado a qual configuração Pin/Tang/TPM2), **`clevis luks regen -d <dev> -s <slot>`** (re-vincula o slot buscando as novas chaves anunciadas pelo servidor Tang após uma rotação!), **`clevis luks edit -d <dev> -s <slot>`** (altera a configuração JSON daquele slot) e **`clevis luks unbind -d <dev> -s <slot>`** (apaga tanto o token quanto o keyslot LUKS correspondente).

## Como funciona
E para volumes secundários de dados que são montados após o boot ou em scripts de manutenção, **`sudo clevis luks unlock -d /dev/sdb1 -n dados_seguros`** destrava o volume imediatamente usando o token Clevis embutido.

## Exemplo
```bash
# Listar todos os vinculos Clevis ativos no volume LUKS2 e regenerar o Keyslot 1 apos rotacao de chaves no servidor Tang
sudo clevis luks list -d /dev/nvme0n1p3
sudo clevis luks regen -q -d /dev/nvme0n1p3 -s 1
```

## Limites e trade-offs
Antes de atualizar o firmware BIOS/UEFI ou o pacote `grub2`/`shim` de um servidor que utiliza o Pin `tpm2` vinculado aos registradores PCR `0,2,4,7`, lembre-se de que a atualização alterará legitimamente os valores dos PCRs no próximo boot; tenha a senha de recuperação pronta ou regenere o vínculo após o reboot.

## Como verificar
Execute `sudo clevis luks pass -d /dev/nvme0n1p3 -s 1` apenas em sessões de diagnóstico seguro se precisar verificar se o Pin consegue recuperar a passphrase do slot `1` no momento atual.

## Conexões
- [[clevis-integracao-luks2-clevis-luks-bind-initramfs-dracut-systemd]] — Veja também: Clevis + LUKS2 (`clevis luks bind`): Desbloqueio Automatizado da Partição Raiz (`/`) no Boot via **`dracut` / `initramfs-tools`** e Rede Pré-Boot.
- [[clevis-pin-tpm2-pcr-banks-sha256-assinatura-politicas-seguranca]] — Veja também: Clevis Pin **`tpm2`**: Seleção Segura de Bancos e Registradores **PCR (`pcr_bank`, `pcr_ids`)** para Integridade de Boot.
- [[clevis-operacao-servidor-tang-rotacao-chaves-jwk-adv-verificacao]] — Referência cruzada direta com clevis-operacao-servidor-tang-rotacao-chaves-jwk-adv-verificacao.
- [[cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey]] — Referência cruzada direta com cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey.

## Fontes
- [Clevis Official GitHub — Automated Decryption Framework & Pins (tang, tpm2, sss, pkcs11)](https://raw.githubusercontent.com/latchset/clevis/master/README.md) — documentação oficial do framework Clevis cobrindo pins tang, tpm2, sss (Shamir Secret Sharing), pkcs11 e integração LUKS2/initramfs; consultado em 2026-10-03.
- [Tang Official GitHub — Stateless Network-Bound Cryptographic Server & ECMR Protocol](https://raw.githubusercontent.com/latchset/tang/master/README.md) — documentação oficial do servidor Tang cobrindo protocolo McCallum-Relyea (ECMR), geração/rotação de chaves JWK e operação stateless; consultado em 2026-10-03.
- [Latchset JOSE Official C Library & CLI Reference](https://github.com/latchset/jose) — repositório oficial da biblioteca e utilitário jose para objetos JWE/JWK/JWS utilizados pelo Clevis e Tang; consultado em 2026-10-03.
