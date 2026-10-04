---
id: software.seguranca.tranche13.001218
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/log2timeline/plaso/main/README.md", "https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Forense de Servidores **Linux, macOS e Containers** com o Plaso: Parsers `syslog`, `systemd_journal`, `utmp`/`wtmp`, `bash_history`, `fsext` e `plist`

## Em uma frase
Quando o incidente ocorre em um servidor **Linux de produção**, um container Docker/Kubernetes ou no **MacBook (macOS)** de um executivo/engenheiro, quais parsers o Plaso aciona automaticamente através dos presets `linux` e `macosx`?

## Por que importa
Em **Linux**, o Plaso correlaciona na mesma linha do tempo: **(1) Metadados de sistema de arquivos (`filestat` / `fsext` / `fsxfs`)** com os 4 timestamps MACB (`mtime`, `atime`, `ctime`, `crtime` *birth time* do ext4/XFS!); **(2) Logs de autenticação e sistema (`syslog`, `systemd_journal` binário `.journal`, `auditd`, `dpkg`/`apt`/`yum`)**; **(3) Registros binários de sessão (`utmp` / `wtmp` / `btmp` / `lastlog`)**; **(4) Artefatos de usuário (`.bash_history`, `.zsh_history`, `.viminfo`, `ssh` known_hosts, `cron`, `atjobs`, `dockerjson`)**; e **(5) Logs de servidores Web (`apache_access`, `nginx`, `vsftpd`)**!

## Como funciona
Em **macOS**, o preset `macosx` extrai arquivos binários e XML **`plist`** (`LaunchAgents`, `LaunchDaemons`), **`fseventsd`** (registro histórico de todas as mudanças de arquivos no APFS/HFS+!), **`ls_quarantine`** (arquivos baixados da internet com a flag `com.apple.quarantine`), **`utmpx`**, **`mac_keychain`**, **`macwifi`** e **`asl_log` / `bsm_log`**!

## Exemplo
```bash
# Gerar uma Super Timeline forense de uma imagem de servidor Linux ou container montado usando o preset 'linux'
log2timeline.py \
  --storage-file ./incidente_servidor_linux.plaso \
  --parsers "linux" \
  --unattended \
  ./evidencias/imagem_disco_ubuntu_prod.raw
```

## Limites e trade-offs
Em sistemas de arquivos **ext4** e **XFS v5** modernos no Linux, o Plaso extrai através do `libfsext` / `libfsxfs` o timestamp de criação real do inode (**`crtime` / *Birth Time***) diretamente da tabela de inodes da imagem bruta — um artefato crucial para detectar exatamente quando um webshell ou binário de rootkit foi gravado no disco, mesmo que o invasor tenha alterado o `mtime` com `touch`!

## Como verificar
Combine a timeline Linux do Plaso com a verificação de hashes do **AIDE** para identificar tanto *o que* foi modificado quanto *a sequência exata de eventos* ao redor da modificação.

## Conexões
- [[plaso-integracao-timesketch-opensearch-psteal-investigacao-colaborativa]] — Veja também: Pipeline Direto **`psteal.py`** e Integração Nativa **Plaso + Google Timesketch (`opensearch_ts`)**: Investigação Forense Colaborativa em Escala.
- [[plaso-forense-navegadores-webhist-chrome-firefox-edge-downloads-cookies]] — Veja também: Reconstrução de **Atividade de Navegadores e Downloads de Malware (`webhist`)** no Plaso: Chrome/Edge (Chromium), Firefox, Safari e Extensões.
- [[plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite]] — Referência cruzada direta com plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite.
- [[aide-resposta-incidentes-forense-linux-rootkits-ld-so-preload-pam]] — Referência cruzada direta com aide-resposta-incidentes-forense-linux-rootkits-ld-so-preload-pam.
- [[atomicredteam-testes-linux-macos-containers-bash-sh-validacao-edr]] — Referência cruzada direta com atomicredteam-testes-linux-macos-containers-bash-sh-validacao-edr.

## Fontes
- [Plaso (`log2timeline`) Official GitHub — Super Timeline All the Things](https://raw.githubusercontent.com/log2timeline/plaso/main/README.md) — repositório oficial do motor forense Plaso cobrindo arquitetura de parsers, plugins de análise, event tagging e formatos de armazenamento; consultado em 2026-10-03.
- [Plaso Official Documentation — Using `log2timeline.py` (`plaso.readthedocs.io`)](https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html) — documentação oficial do Plaso detalhando extração de imagens E01/RAW, partições, Volume Shadow Copies (`--vss_stores`), BitLocker, presets de parsers e arquitetura multi-worker; consultado em 2026-10-03.
