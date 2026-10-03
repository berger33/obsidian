---
id: software.seguranca.tranche04.000312
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

# ClamAV: Configuração do `clamd.conf`, Protocolo `INSTREAM` e Limites Anti-Zip-Bomb

## Em uma frase
O arquivo `clamd.conf` governa os sockets de escuta (`LocalSocket` Unix ou `TCPSocket`), o pool de threads (`MaxThreads`) e os limites defensivos de descompressão do daemon `clamd`.

## Por que importa
Impede que arquivos malformados ou bombas de descompressão (*zip bombs* / *billion laughs*) esgotem a memória ou travem as threads de inspeção do servidor de segurança.

## Como funciona
Microserviços remotos enviam buffers de arquivos em memória diretamente ao `clamd` via comando `zINSTREAM\0` sobre TCP (porta `3310`) sem compartilhar disco. Parâmetros como `MaxScanSize`, `MaxFileSize`, `MaxRecursion` e `MaxFiles` limitam rigorosamente a profundidade de arquivos compactados aninhados e o volume total extraído por varredura.

## Exemplo
```ini
# /etc/clamav/clamd.conf
LocalSocket /run/clamav/clamd.ctl
LocalSocketMode 660
TCPSocket 3310
TCPAddr 127.0.0.1
MaxThreads 16
MaxScanSize 150M
MaxFileSize 50M
MaxRecursion 16
MaxFiles 10000
AlertExceededMax yes
```

## Limites e trade-offs
Expor `TCPSocket 3310` em interfaces de rede sem firewall permite que qualquer host envie comandos `SHUTDOWN` ou `RELOAD` não autenticados ao `clamd`; restrinja `TCPAddr` ou use `NetworkPolicy`/mTLS.

## Como verificar
Envie `printf "zPING\0" | nc -U /run/clamav/clamd.ctl` e confirme o retorno `PONG`, verificando também os limites ativos com `clamconf | grep -E "MaxScanSize|MaxRecursion"`.

## Conexões
- [[clamav-arquitetura-libclamav-clamd-clamscan-freshclam]] — Veja também: ClamAV: Arquitetura do Motor `libclamav`, Daemon `clamd`, `clamscan` e `freshclam`.
- [[clamav-atualizacao-freshclam-cvd-cld-private-local-mirrors]] — Veja também: ClamAV: Atualização Segura de Bases (`freshclam`), Arquivos `.cvd`/`.cld` e Mirrors Privados.
- [[clamav-monitoramento-performance-clamdtop-filas-threads-memoria]] — Referência cruzada direta com clamav-monitoramento-performance-clamdtop-filas-threads-memoria.
- [[clamav-integracao-pipelines-upload-api-milter-icap-s3]] — Referência cruzada direta com clamav-integracao-pipelines-upload-api-milter-icap-s3.

## Fontes
- [Cisco ClamAV Official Documentation — Usage Manual (libclamav Architecture, clamd, clamdscan, clamonacc, freshclam, sigtool & clambc)](https://raw.githubusercontent.com/Cisco-Talos/clamav/main/README.md) — Manual oficial de uso do ClamAV detalhando o fluxo de varredura cliente/servidor do clamd, utilitários de banco e configuração; consultado em 2026-10-03.
- [Cisco ClamAV GitHub — README.md (Open-Source Antivirus Engine Overview, Signatures, Packaging & Licensing)](https://docs.clamav.net/manual/Usage.html) — README oficial do Cisco-Talos/clamav descrevendo a arquitetura da engine, suporte multiplataforma e documentação de assinaturas; consultado em 2026-10-03.
- [Cisco ClamAV Official Documentation — Signature Writing Manual](https://docs.clamav.net/manual/Signatures.html) — Manual oficial de criação de assinaturas customizadas, lógicas, bytecode e YARA no ClamAV; consultado em 2026-10-03.
