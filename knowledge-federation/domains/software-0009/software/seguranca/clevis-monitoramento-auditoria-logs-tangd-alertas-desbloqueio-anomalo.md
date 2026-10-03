---
id: software.seguranca.tranche08.000740
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

# Observabilidade e Detecção de Intrusão no **Tang / NBDE**: Monitoramento de Requisições `POST /rec/` e Alertas de Desbloqueio Fora de Janela

## Em uma frase
Toda vez que um servidor protegido por Clevis/Tang reinicia (ou quando alguém tenta decifrar o objeto JWE do cabeçalho LUKS2), o cliente precisa obrigatoriamente enviar uma requisição **`POST /rec/<kid>`** para o servidor Tang: isso transforma os logs de acesso do servidor Tang em um **sensor de alta fidelidade de reinicialização e tentativa de desbloqueio de discos de toda a frota**!

## Por que importa
Se um invasor que obteve acesso a um host do datacenter copiar o cabeçalho LUKS2 (`dd if=/dev/sda3 count=32768`) de outro servidor e tentar usar o comando `clevis decrypt` a partir de um IP inesperado, ou se um servidor crítico tentar desbloquear seu disco às 03:00 da manhã sem que tenha havido reboot programado, o log do `tangd` / proxy reverso registra o IP de origem e o `<kid>` exato.

## Como funciona
Encaminhar os logs do `tangd.socket` / `journald` para o SIEM / Suricata e correlacionar cada `POST /rec/<kid>` com eventos legítimos de boot do servidor permite detectar imediatamente qualquer tentativa de decriptação offline não-autorizada dentro da LAN.

## Exemplo
```bash
# Inspecionar no journald todas as conexoes e operacoes atendidas pelo socket-activated tangd
sudo journalctl -u "tangd@*" -u tangd.socket --since "24 hours ago"
```

## Limites e trade-offs
Para máxima rastreabilidade, você pode gerar pares de chaves Tang separados por zona de segurança ou monitorar no proxy local os `kid` requisitados em `/rec/<kid>` correlacionando-os com o inventário de servidores.

## Como verificar
Configure uma regra de alerta no SIEM sempre que um endpoint `/rec/<kid>` do servidor Tang for chamado a partir de um endereço IP que não conste na lista estática de IPs dos servidores com LUKS/Clevis.

## Conexões
- [[clevis-seguranca-rede-tang-segmentacao-vlan-ipsec-wireguard-mtls]] — Veja também: Arquitetura de Segurança de Rede para **Tang (NBDE)**: Segmentação de VLAN de Boot, *802.1X MACsec* e Riscos de Exposição do Endpoint `/rec`.
- [[clevis-arquitetura-nbde-tang-mccallum-relyea-ecmr-sem-escrow]] — Referência cruzada direta com clevis-arquitetura-nbde-tang-mccallum-relyea-ecmr-sem-escrow.

## Fontes
- [Clevis Official GitHub — Automated Decryption Framework & Pins (tang, tpm2, sss, pkcs11)](https://raw.githubusercontent.com/latchset/clevis/master/README.md) — documentação oficial do framework Clevis cobrindo pins tang, tpm2, sss (Shamir Secret Sharing), pkcs11 e integração LUKS2/initramfs; consultado em 2026-10-03.
- [Tang Official GitHub — Stateless Network-Bound Cryptographic Server & ECMR Protocol](https://raw.githubusercontent.com/latchset/tang/master/README.md) — documentação oficial do servidor Tang cobrindo protocolo McCallum-Relyea (ECMR), geração/rotação de chaves JWK e operação stateless; consultado em 2026-10-03.
- [Latchset JOSE Official C Library & CLI Reference](https://github.com/latchset/jose) — repositório oficial da biblioteca e utilitário jose para objetos JWE/JWK/JWS utilizados pelo Clevis e Tang; consultado em 2026-10-03.
