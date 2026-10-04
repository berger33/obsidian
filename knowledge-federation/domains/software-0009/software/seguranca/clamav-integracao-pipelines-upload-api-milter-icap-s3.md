---
id: software.seguranca.tranche04.000318
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

# ClamAV: Integração em Gateways de E-mail (`clamav-milter`), Servidores ICAP e Eventos S3/API

## Em uma frase
O ClamAV integra-se nativamente a servidores SMTP Postfix/Sendmail via `clamav-milter`, a proxies corporativos/WAFs via adaptadores ICAP (`c-icap-clamav`) e a pipelines de upload em nuvem (S3/MinIO/Kubernetes) via sidecars TCP `INSTREAM`.

## Por que importa
Garante que nenhum anexo de e-mail ou arquivo enviado por usuários externos seja disponibilizado para consumo da aplicação ou de outros usuários antes de receber um veredito `OK` do scanner.

## Como funciona
No Postfix, o `clamav-milter` intercepta a mensagem SMTP em trânsito, encaminha os anexos ao `clamd` e aplica a ação configurada (`OnInfected Reject` ou `Quarantine`). Em arquiteturas de armazenamento de objetos (AWS S3 ou MinIO), um worker assíncrono consome eventos `ObjectCreated`, faz *stream* do objeto para o container `clamd:3310` e aplica a tag `av-status=CLEAN` ou move o objeto infectado para um bucket de quarentena isolado.

## Exemplo
```ini
# /etc/clamav/clamav-milter.conf integrado ao Postfix e ao daemon clamd
MilterSocket inet:8893@127.0.0.1
ClamdSocket unix:/run/clamav/clamd.ctl
OnInfected Reject
OnFail Defer
AddHeader Replace
LogInfected Full
```

## Limites e trade-offs
Configurar `OnFail Accept` no `clamav-milter` ou no gateway de upload permite que malwares atravessem livremente caso o daemon `clamd` seja morto pelo OOM Killer; prefira `OnFail Defer` (HTTP 503 / SMTP 4xx temporário) para falhar de forma segura.

## Como verificar
Envie um anexo de teste contendo a string de verificação EICAR pelo pipeline de upload ou gateway SMTP e confirme a rejeição imediata e o registro do evento no log de auditoria.

## Conexões
- [[clamav-heuristicas-dlp-macros-ole2-pdf-encrypted-archives]] — Veja também: ClamAV: Alertas Heurísticos, Bloqueio de Macros OLE2, Arquivos Criptografados e Prevenção de DLP.
- [[clamav-monitoramento-performance-clamdtop-filas-threads-memoria]] — Veja também: ClamAV: Monitoramento Operacional com `clamdtop`, Pool de Memória e Dimensionamento em Containers.
- [[clamav-arquitetura-libclamav-clamd-clamscan-freshclam]] — Referência cruzada direta com clamav-arquitetura-libclamav-clamd-clamscan-freshclam.
- [[clamav-daemon-clamd-conf-unix-socket-tcp-instream-limites]] — Referência cruzada direta com clamav-daemon-clamd-conf-unix-socket-tcp-instream-limites.

## Fontes
- [Cisco ClamAV Official Documentation — Usage Manual (libclamav Architecture, clamd, clamdscan, clamonacc, freshclam, sigtool & clambc)](https://raw.githubusercontent.com/Cisco-Talos/clamav/main/README.md) — Manual oficial de uso do ClamAV detalhando o fluxo de varredura cliente/servidor do clamd, utilitários de banco e configuração; consultado em 2026-10-03.
- [Cisco ClamAV GitHub — README.md (Open-Source Antivirus Engine Overview, Signatures, Packaging & Licensing)](https://docs.clamav.net/manual/Usage.html) — README oficial do Cisco-Talos/clamav descrevendo a arquitetura da engine, suporte multiplataforma e documentação de assinaturas; consultado em 2026-10-03.
- [Cisco ClamAV Official Documentation — Signature Writing Manual](https://docs.clamav.net/manual/Signatures.html) — Manual oficial de criação de assinaturas customizadas, lógicas, bytecode e YARA no ClamAV; consultado em 2026-10-03.
