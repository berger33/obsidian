---
id: software.seguranca.tranche04.000313
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/Cisco-Talos/clamav/main/README.md", "https://docs.clamav.net/manual/Usage.html", "https://docs.clamav.net/manual/Signatures.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ClamAV: Atualização Segura de Bases (`freshclam`), Arquivos `.cvd`/`.cld` e Mirrors Privados

## Em uma frase
O utilitário e daemon `freshclam` baixa e verifica criptograficamente atualizações incrementais (`.cdiff`) e bancos completos (`main.cvd`, `daily.cvd`, `bytecode.cvd`) a partir da CDN oficial ou de mirrors internos.

## Por que importa
Frotas com dezenas de nós ou containers realizando download direto da CDN pública sofrem *rate-limiting* (HTTP 429/403) por IP compartilhado; o uso de um mirror privado local resolve o bloqueio e permite ambientes *air-gapped*.

## Como funciona
O `freshclam` consulta registros DNS TXT (`current.cvd.clamav.net`) para descobrir se há novas versões antes de baixar deltas `.cdiff` para atualizar arquivos `.cld` locais e notificar o `clamd` via `NotifyClamd /etc/clamav/clamd.conf`. Em redes corporativas, a ferramenta `cvdupdate` hospeda um espelho HTTP interno alimentando `PrivateMirror` nos clientes.

## Exemplo
```ini
# /etc/clamav/freshclam.conf configurado com mirror interno e reload automático do clamd
DatabaseDirectory /var/lib/clamav
UpdateLogFile /var/log/clamav/freshclam.log
Checks 24
PrivateMirror https://clamav-mirror.internal.corp/cvds
ScriptedUpdates yes
NotifyClamd /etc/clamav/clamd.conf
```

## Limites e trade-offs
Ao usar `PrivateMirror`, o `freshclam` desativa automaticamente consultas DNS TXT públicas e downloads `.cdiff` se `ScriptedUpdates no` for definido, exigindo que o mirror interno sirva os arquivos `.cvd` completos e `dns.txt`.

## Como verificar
Execute `freshclam --verbose` e inspecione `sigtool --info /var/lib/clamav/daily.cld` (ou `.cvd`) para confirmar a data de compilação recente e a validação da assinatura digital.

## Conexões
- [[clamav-daemon-clamd-conf-unix-socket-tcp-instream-limites]] — Veja também: ClamAV: Configuração do `clamd.conf`, Protocolo `INSTREAM` e Limites Anti-Zip-Bomb.
- [[clamav-varredura-tempo-real-clamonacc-fanotify-on-access-linux]] — Veja também: ClamAV: Varredura On-Access em Tempo Real (`clamonacc`) via Linux `fanotify`.
- [[clamav-arquitetura-libclamav-clamd-clamscan-freshclam]] — Referência cruzada direta com clamav-arquitetura-libclamav-clamd-clamscan-freshclam.
- [[clamav-assinaturas-customizadas-hdb-ndb-ldb-yara-sigtool]] — Referência cruzada direta com clamav-assinaturas-customizadas-hdb-ndb-ldb-yara-sigtool.

## Fontes
- [Cisco ClamAV Official Documentation — Usage Manual (libclamav Architecture, clamd, clamdscan, clamonacc, freshclam, sigtool & clambc)](https://raw.githubusercontent.com/Cisco-Talos/clamav/main/README.md) — Manual oficial de uso do ClamAV detalhando o fluxo de varredura cliente/servidor do clamd, utilitários de banco e configuração; consultado em 2026-10-03.
- [Cisco ClamAV GitHub — README.md (Open-Source Antivirus Engine Overview, Signatures, Packaging & Licensing)](https://docs.clamav.net/manual/Usage.html) — README oficial do Cisco-Talos/clamav descrevendo a arquitetura da engine, suporte multiplataforma e documentação de assinaturas; consultado em 2026-10-03.
- [Cisco ClamAV Official Documentation — Signature Writing Manual](https://docs.clamav.net/manual/Signatures.html) — Manual oficial de criação de assinaturas customizadas, lógicas, bytecode e YARA no ClamAV; consultado em 2026-10-03.
