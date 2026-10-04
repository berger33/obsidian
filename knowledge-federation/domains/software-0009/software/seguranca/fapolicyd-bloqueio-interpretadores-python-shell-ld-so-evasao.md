---
id: software.seguranca.tranche15.001437
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md", "https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Blindando Interpretadores (**Python, Perl, Ruby, PHP, Lua, Node.js e Bash**) e Bloqueando Evasões `ld.so` / `/dev/shm` no fapolicyd

## Em uma frase
Um erro fatal de muitos sistemas antigos de Application Whitelisting era olhar apenas para o binário executável ELF (`/usr/bin/python3` ou `/usr/bin/bash`): como `/usr/bin/python3` é um binário assinado e confiável da distribuição, qualquer invasor podia rodar `python3 /tmp/ransomware.py` ou `python3 -c "import os..."` e passar direto pela whitelist!

## Por que importa
Como o **`fapolicyd`** fecha essa brecha inspecionando **Scripts Interpretados, Bytecode e Bibliotecas Compartilhadas**?

## Como funciona
Porque o `fapolicyd` intercepta no `fanotify` não apenas `perm=execute` (`FAN_OPEN_EXEC_PERM`), mas também **`perm=open` (`FAN_OPEN_PERM`)**! Quando o sujeito `exe=/usr/bin/python3` (ou `perl`, `ruby`, `php`, `lua`, `bash`) tenta abrir (`perm=open`) um arquivo cujo MIME type detectado pelo `libmagic` do `fapolicyd` é `text/x-python`, `application/x-bytecode.python`, `text/x-shellscript` ou `application/x-sharedlib`, as regras `41-shared-obj.rules` e `70-trusted-lang.rules` exigem que **o próprio arquivo `.py`, `.pyc`, `.sh` ou `.so` aberto também tenha `trust=1` no banco LMDB**! Se o script estiver em `/tmp/ransomware.py` (`trust=0`), o Kernel recebe `EPERM (Operation not permitted)` e o Python nem consegue ler o arquivo!

## Exemplo
```bash
# Testar a deteccao de MIME type (ftype) do fapolicyd sobre um binario ELF, uma biblioteca compartilhada .so e um script Python
fapolicyd-cli --ftype /usr/bin/ls
fapolicyd-cli --ftype /usr/lib64/libc.so.6 || fapolicyd-cli --ftype /lib/x86_64-linux-gnu/libc.so.6
```

## Limites e trade-offs
E se um desenvolvedor tentar instalar pacotes Python com `pip install --user` dentro de `~/.local/lib/python3.*/site-packages/` em um servidor protegido pelo `fapolicyd`? Como arquivos baixados pelo `pip` na pasta home do usuário têm `trust=0` (e muitas bibliotecas Python como `numpy` ou `cryptography` trazem extensões C `.so` compiladas!), o `fapolicyd` bloqueará o carregamento dessas `.so` e `.py` não confiáveis!

## Como verificar
Em servidores de produção com `fapolicyd`, instale bibliotecas Python via pacotes oficiais do sistema (`rpm`/`deb`) ou em um ambiente virtual imutável em `/opt/app/venv` pertencente a `root` e registrado com `fapolicyd-cli --file add /opt/app/venv --trust-file app-venv`!

## Conexões
- [[fapolicyd-modo-permissivo-debug-deny-testes-seguros-producao]] — Veja também: Testando Políticas sem Risco de Lockout no fapolicyd: Modo **`--permissive`**, Diagnóstico **`--debug-deny`** e Interpretação dos Eventos de Negação.
- [[fapolicyd-tuning-performance-watch-fs-q-size-caches-containers]] — Veja também: Tuning de Performance do **`/etc/fapolicyd/fapolicyd.conf`**: Sistemas de Arquivos Monitorados (`watch_fs`), `ignore_mounts`, Tamanho de Fila `q_size` e Cache Hit Ratio.
- [[fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb]] — Referência cruzada direta com fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb.
- [[fapolicyd-politicas-known-libs-restrictive-fagenrules-rules-d]] — Referência cruzada direta com fapolicyd-politicas-known-libs-restrictive-fagenrules-rules-d.
- [[fapolicyd-gerenciamento-trust-database-fapolicyd-cli-file-add-trust-d]] — Referência cruzada direta com fapolicyd-gerenciamento-trust-database-fapolicyd-cli-file-add-trust-d.

## Fontes
- [Official `fapolicyd` GitHub Repository (`linux-application-whitelisting/fapolicyd`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md) — repositório oficial do File Access Policy Daemon cobrindo interceptação de execução via `fanotify`, linguagem de regras `allow`/`deny_audit`, `fapolicyd-cli` e banco de confiança; consultado em 2026-10-03.
- [Official `fapolicyd.conf` Configuration Specification (`init/fapolicyd.conf`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf) — especificação oficial de configuração do `/etc/fapolicyd/fapolicyd.conf` detalhando `permissive`, `trust = rpmdb,file`, `integrity = none|size|ima|sha256`, `watch_fs` e caches LRU; consultado em 2026-10-03.
