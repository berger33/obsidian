---
id: software.seguranca.tranche04.000311
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

# ClamAV: Arquitetura do Motor `libclamav`, Daemon `clamd`, `clamscan` e `freshclam`

## Em uma frase
ClamAV (Cisco Talos, GPLv2) é o motor antivírus open-source padrão para inspeção de malware, trojans e artefatos maliciosos em gateways de e-mail, pipelines de upload de arquivos e servidores Linux/containers.

## Por que importa
Fornece inspeção profunda de dezenas de formatos de arquivo (PE, ELF, Mach-O, PDF, Office OLE2/OOXML, ZIP/7z/TAR) descompactando recursivamente containers antes de aplicar assinaturas e heurísticas.

## Como funciona
A biblioteca central `libclamav` pode ser invocada em modo *one-shot* pelo utilitário `clamscan` (que carrega o banco de assinaturas na RAM a cada execução) ou mantida residente na memória pelo daemon multi-thread `clamd`, que atende requisições rápidas de clientes leves como `clamdscan`, `clamonacc` e `clamav-milter`, enquanto o `freshclam` sincroniza os bancos `.cvd`/`.cld`.

## Exemplo
```bash
# Verificar configuração consolidada do ClamAV e estado dos bancos de assinaturas
clamconf -n

# Executar varredura rápida via socket do daemon clamd passando descritor de arquivo
clamdscan --fdpass --multiscan /var/spool/uploads/
```

## Limites e trade-offs
Invocar `clamscan` diretamente a cada upload HTTP em produção consome centenas de megabytes de RAM e vários segundos de CPU por chamada para compilar o banco de assinaturas; use sempre `clamd` + `clamdscan` ou protocolo TCP/Unix socket.

## Como verificar
Execute `clamdscan --ping 3` e `clamconf` para validar que o daemon `clamd` responde imediatamente com as bases `main.cvd`, `daily.cvd` e `bytecode.cvd` carregadas.

## Conexões
- [[clamav-daemon-clamd-conf-unix-socket-tcp-instream-limites]] — Veja também: ClamAV: Configuração do `clamd.conf`, Protocolo `INSTREAM` e Limites Anti-Zip-Bomb.
- [[clamav-atualizacao-freshclam-cvd-cld-private-local-mirrors]] — Referência cruzada direta com clamav-atualizacao-freshclam-cvd-cld-private-local-mirrors.
- [[clamav-varredura-tempo-real-clamonacc-fanotify-on-access-linux]] — Referência cruzada direta com clamav-varredura-tempo-real-clamonacc-fanotify-on-access-linux.

## Fontes
- [Cisco ClamAV Official Documentation — Usage Manual (libclamav Architecture, clamd, clamdscan, clamonacc, freshclam, sigtool & clambc)](https://raw.githubusercontent.com/Cisco-Talos/clamav/main/README.md) — Manual oficial de uso do ClamAV detalhando o fluxo de varredura cliente/servidor do clamd, utilitários de banco e configuração; consultado em 2026-10-03.
- [Cisco ClamAV GitHub — README.md (Open-Source Antivirus Engine Overview, Signatures, Packaging & Licensing)](https://docs.clamav.net/manual/Usage.html) — README oficial do Cisco-Talos/clamav descrevendo a arquitetura da engine, suporte multiplataforma e documentação de assinaturas; consultado em 2026-10-03.
- [Cisco ClamAV Official Documentation — Signature Writing Manual](https://docs.clamav.net/manual/Signatures.html) — Manual oficial de criação de assinaturas customizadas, lógicas, bytecode e YARA no ClamAV; consultado em 2026-10-03.
