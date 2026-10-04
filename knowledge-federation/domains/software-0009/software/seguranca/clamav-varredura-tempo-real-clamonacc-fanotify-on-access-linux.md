---
id: software.seguranca.tranche04.000314
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

# ClamAV: Varredura On-Access em Tempo Real (`clamonacc`) via Linux `fanotify`

## Em uma frase
O daemon `clamonacc` provê proteção em tempo real (*On-Access Scanning*) em servidores Linux interceptando eventos de abertura e execução de arquivos no kernel via API `fanotify` e submetendo-os ao `clamd`.

## Por que importa
Permite bloquear sincronicamente (`OnAccessPrevention yes`) a leitura ou execução de um webshell ou binário malicioso recém-gravado no disco antes que o processo solicitante receba o descritor de arquivo.

## Como funciona
O `clamonacc` registra marcas `fanotify` nos diretórios ou pontos de montagem configurados (`OnAccessIncludePath` / `OnAccessMountPath`). Sempre que um processo fora da lista de exclusão (`OnAccessExcludeUname clamav`) abre ou fecha um arquivo modificado, o `clamonacc` envia o arquivo ao `clamd` e, em caso de infecção, nega a syscall `open()` (`EACCES`) e move/remove o artefato se configurado.

## Exemplo
```ini
# Trecho do /etc/clamav/clamd.conf para On-Access Scanning com prevenção ativa
OnAccessIncludePath /var/www/uploads
OnAccessIncludePath /home
OnAccessExcludeUname clamav
OnAccessPrevention yes
OnAccessExtraScanning yes
OnAccessMaxFileSize 25M
```

## Limites e trade-offs
Habilitar `OnAccessMountPath /` com `OnAccessPrevention yes` ao mesmo tempo é incompatível no `fanotify` e pode causar *deadlock* no sistema operacional se o próprio `clamd` ou bibliotecas do sistema forem interceptados.

## Como verificar
Inicie `clamonacc --foreground --log=/var/log/clamav/clamonacc.log`, grave um arquivo de teste com a string padrão EICAR em `/var/www/uploads` e confirme que a leitura subsequente é negada pelo kernel.

## Conexões
- [[clamav-atualizacao-freshclam-cvd-cld-private-local-mirrors]] — Veja também: ClamAV: Atualização Segura de Bases (`freshclam`), Arquivos `.cvd`/`.cld` e Mirrors Privados.
- [[clamav-assinaturas-customizadas-hdb-ndb-ldb-yara-sigtool]] — Veja também: ClamAV: Escrita de Assinaturas Customizadas (`.hdb`, `.hsb`, `.ndb`, `.ldb`, `.yar`) e `sigtool`.
- [[clamav-arquitetura-libclamav-clamd-clamscan-freshclam]] — Referência cruzada direta com clamav-arquitetura-libclamav-clamd-clamscan-freshclam.
- [[clamav-daemon-clamd-conf-unix-socket-tcp-instream-limites]] — Referência cruzada direta com clamav-daemon-clamd-conf-unix-socket-tcp-instream-limites.
- [[clamav-heuristicas-dlp-macros-ole2-pdf-encrypted-archives]] — Referência cruzada direta com clamav-heuristicas-dlp-macros-ole2-pdf-encrypted-archives.

## Fontes
- [Cisco ClamAV Official Documentation — Usage Manual (libclamav Architecture, clamd, clamdscan, clamonacc, freshclam, sigtool & clambc)](https://raw.githubusercontent.com/Cisco-Talos/clamav/main/README.md) — Manual oficial de uso do ClamAV detalhando o fluxo de varredura cliente/servidor do clamd, utilitários de banco e configuração; consultado em 2026-10-03.
- [Cisco ClamAV GitHub — README.md (Open-Source Antivirus Engine Overview, Signatures, Packaging & Licensing)](https://docs.clamav.net/manual/Usage.html) — README oficial do Cisco-Talos/clamav descrevendo a arquitetura da engine, suporte multiplataforma e documentação de assinaturas; consultado em 2026-10-03.
- [Cisco ClamAV Official Documentation — Signature Writing Manual](https://docs.clamav.net/manual/Signatures.html) — Manual oficial de criação de assinaturas customizadas, lógicas, bytecode e YARA no ClamAV; consultado em 2026-10-03.
