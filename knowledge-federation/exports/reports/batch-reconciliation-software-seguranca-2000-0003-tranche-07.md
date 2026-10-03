# Relatório de Reconciliação de Lote — `software-seguranca-2000-0003` (Tranche 07: IDs 601–700)

- **Data:** `2026-10-03`
- **Lote:** `software-seguranca-2000-0003` (`knowledge-federation/domains/software-0009/software/seguranca/`)
- **Status do lote:** `in_progress` (`700 / 2.000` — `35,00%`)
- **Tranche concluída:** `Tranche 07` (IDs `0601–0700`, `100` notas técnicas substantivas)
- **Lotes concluídos globalmente:** `2 / 500` (`software-testes-2000-0001` e `software-devops-2000-0002`)
- **Notas válidas contabilizadas globalmente:** `4.740 / 1.000.000` (`0,4740%`)
  - **Aprovadas por revisão humana:** `49` (históricas preservadas)
  - **Aprovadas por revisão factual de IA:** `4.691` (`1.991` Testes + `2.000` DevOps + `700` Segurança + `40` Fundamentos/Legado)
- **Total de arquivos `.md` em `knowledge-federation/domains/`:** `4.840` (`4.740` válidas + `100` legadas pendentes fora dos lotes ativos)

## Resumo da Tranche 07 (`0601–0700`)

1. **`testssl.sh` (`0601–0610`)**: `10` notas sobre auditoria de servidores TLS/SSL em qualquer porta TCP, protocolos (`-p`), Forward Secrecy/ML-KEM (`-f`), cadeia X.509/OCSP/CAA (`-S`), vulnerabilidades criptográficas (`-U`), `STARTTLS` (`-t`), cabeçalhos HTTP (`-h`), simulação de clientes (`-c`), varredura em massa (`--file`) e `--mtls`.
2. **EFF Certbot & Protocolo ACME (`0611–0620`)**: `10` notas sobre RFC 8555, desafios `HTTP-01` (`--webroot`/`--standalone`) e `DNS-01` (delegação `CNAME` `acme-dns`), `certbot renew` com `--deploy-hook`, chaves ECDSA (`secp256r1`/`secp384r1`), ARI e revogação (`keycompromise`), EAB, registros DNS CAA (`RFC 8659`/`RFC 8657`), perfis TLS Mozilla e containers *non-root*.
3. **Hashcat (`0621–0630`)**: `10` notas sobre arquitetura GPU e *In-Kernel Rule Engine*, modos de ataque (`-a 0,1,3,6,7,9`), linguagem de regras (`-r`), máscaras e cadeias de Markov (`-a 3`), auditoria de Active Directory (`-m 1000`, `-m 5600`, `-m 13100`, `-m 18200`, `-m 2100`), *Hashcat Brain*, *Assimilation Bridge*, PCFG/`-S`, mapeamento de teclado FDE e defesa com **Argon2id (RFC 9106)**.
4. **NSA Ghidra (`0631–0640`)**: `10` notas sobre SLEIGH e representação intermediária **P-Code**, fluxo de dados SSA (`Varnode`/`PcodeOp`), automação `analyzeHeadless`, scripting nativo CPython 3 (`PyGhidra`), reconstrução de tipos/C++ (`RTTI`/`vtable`/PDB/DWARF), `FunctionID`/`BSim`, firmware bare-metal (CMSIS-SVD), `EmulatorHelper`, `GhidraServer`/`Version Tracking` e `Ghidra Debugger`.
5. **Radare2 (`r2`) (`0641–0650`)**: `10` notas sobre arquitetura Unix-first e JSON (`j`), triagem de mitigações com `rabin2` (`canary`, `nx`, `pic`, `relro`), grafos CFG (`agf`) e `r2ghidra` (`pdg`), emulação **ESIL**, *Patch Diffing* com `radiff2`/`Zignatures`, entropia por blocos com `rahash2`, `rasm2`/`rax2`, `r2pipe`, depuração reversível (`dts+`/`dtsc`/`dtsr`, `rarun2`, `r2frida`) e geração de YARA mascarado (`aoj`).
6. **Frida (`0651–0660`)**: `10` notas sobre `frida-core`/`frida-gum` (QuickJS/V8), `Interceptor.attach`/`NativeFunction`, rastreamento com **`Stalker`** e **`CModule`**, pontes mobile `Java.perform` e `ObjC.classes`, `Memory.scan`/`MemoryAccessMonitor`/`ApiResolver`, `frida-trace`, `rpc.exports`, operação sem root com `frida-gadget`, desempacotamento em memória e `Cloak`.
7. **Fail2ban (`0661–0670`)**: `10` notas sobre precedência `.conf` vs `.local`, jails (`backend = systemd`), escrita de filtros seguros contra **ReDoS** e *Log Injection* (`<ADDR>`, `usedns = no`), benchmark com `fail2ban-regex`, sets `nftables`/`ipset`, `bantime.increment` e `recidive`, proxies reversos (`set_real_ip_from`), correlação multi-linha (`<F-MLFID>`), webhooks SOC, `fail2ban-client` e defesa em profundidade.
8. **Sudo (`sudo` & `sudo_logsrvd`) (`0671–0680`)**: `10` notas sobre plugins (`sudo.conf`, `visudo -c -s`), precedência *Last Match Wins*, pinagem criptográfica **SHA-256 Digest**, prevenção de *GTFOBins* (`NOEXEC:`, `sudoedit`, proibição de `*` aberto), hardening `Defaults` (`env_reset`, `secure_path`, `use_pty`), gravação I/O (`sudoreplay`), `sudo_logsrvd` mTLS, `python_plugin.so`, confinamento SELinux/AppArmor e modo `04750`.
9. **Bubblewrap (`bwrap`) (`0681–0690`)**: `10` notas sobre sandboxing sem privilégios (`CLONE_NEWUSER`, `PR_SET_NO_NEW_PRIVS`), filesystem zero-trust (`--ro-bind`, `--tmpfs`), isolamento de namespaces (`--unshare-all`, `--unshare-net`, `--disable-userns`), proteção contra `TIOCSTI` (`CVE-2017-5226` via `--new-session` e `--die-with-parent`), `--seccomp FD`, `--clearenv`, bloqueio de sockets D-Bus/X11 (`xdg-dbus-proxy`), `--json-status-fd`, `--ro-bind-data` e limites cgroups v2 (`systemd-run`).
10. **Project Quay Clair v4 & `ClairCore` (`0691–0700`)**: `10` notas sobre arquitetura (`Indexer`, `Matcher`, `Notifier`), indexação content-addressable OCI (`IndexReport`), scanners de pacotes de SO e linguagens (`gobin`, `python`, `java`), matching sem falsos positivos de *backporting* (OVAL, OSV, CSAF/VEX, CVSS), `Notifier` webhooks, `clairctl` (`export-updaters`/`import-updaters`), modos `combo` vs microsserviços com PostgreSQL Advisory Locks, JWT `auth.psk`, `normalized_severity` e integração com Project Quay/Kubernetes.

## Verificações Executadas

- `audit_note_quality.py` (lote `software-0009` e global `knowledge-federation/domains/`): `700 / 700` válidas no lote (`0` erros de gate), `4.740` válidas globalmente (`4.840` arquivos `.md` totais).
- `global_audit_fast.py`: sincronizado com `4.740` notas válidas (`49` humanas + `4.691` IA).
- Testes unitários (`python3 -m unittest discover -s knowledge-federation/tests`): `12 / 12` OK.
- Similaridade Jaccard de *shingles* de 5 palavras no lote: `< 0.15` e `0` sentenças substantivas duplicadas na tranche.
- Verificação de wikilinks e links Markdown relativos: `0` links quebrados.
