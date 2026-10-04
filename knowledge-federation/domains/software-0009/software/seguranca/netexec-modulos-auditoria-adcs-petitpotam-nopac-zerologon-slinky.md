---
id: software.seguranca.tranche06.000598
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/Pennyw0rth/NetExec/main/README.md", "https://www.netexec.wiki/getting-started/installation", "https://github.com/Pennyw0rth/NetExec"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# NetExec: Catálogo de Módulos (`-M` / `--list-modules`) para Auditoria de **AD CS**, **Coerção RPC** (`coerce_plus`), **WebDAV** e **LAPS**

## Em uma frase
Todo protocolo no NetExec possui um sistema de plugins extensível acionado pela flag **`-M <modulo>`** (listáveis com `nxc <protocolo> -L` e com opções detalhadas via `nxc <protocolo> -M <modulo> --options`).

## Por que importa
Permite verificar em lote dezenas de vulnerabilidades de configuração de Active Directory sem precisar rodar scripts separados: por exemplo, **`-M adcs`** (no `ldap`) enumera todas as Autoridades Certificadoras Enterprise (`pKIEnrollmentService`) e templates de certificados publicados; **`-M coerce_plus`** (no `smb`) verifica se os servidores estão vulneráveis a coerção de autenticação RPC (`PetitPotam` MS-EFSR, `PrinterBug` MS-RPRN, `DFSCoerce` MS-DFSNM, `MSEven`); **`-M webdav`** verifica se o serviço *WebClient* está rodando nas estações (o que permite coerção HTTP sobre SMB); e **`-M laps`** audita permissões de leitura de senhas LAPS v1/v2.

## Como funciona
Opções específicas para cada módulo são passadas com `-o CHAVE=VALOR` (ex.: `-M spider_plus -o READ_ONLY=true` para catalogar metadados de arquivos em compartilhamentos SMB sem baixar os arquivos).

## Exemplo
```bash
# Listar todos os modulos de auditoria disponiveis para SMB e LDAP e auditar servidores AD CS e servico WebClient
nxc ldap -L
nxc ldap dc01.corp.internal -k --use-kcache -M adcs
nxc smb 10.10.20.0/24 -u 'sec_auditor' -p 'AuditPass!2026' -M webdav
```

## Limites e trade-offs
Antes de executar qualquer módulo desconhecido com `-M`, rode sempre **`nxc <proto> -M <modulo> --options`** e verifique a coluna `OPSEC SAFE` e se o módulo faz alterações no sistema ou apenas leitura.

## Como verificar
Execute `nxc smb <SUBNET> -u <user> -p <pass> -M webdav` para identificar estações que estão com o serviço `WebClient` ativo e desative o serviço via GPO se WebDAV não for utilizado.

## Conexões
- [[netexec-protocolos-mssql-ssh-rdp-ftp-vnc-auditoria-multi-servico]] — Veja também: NetExec (`nxc mssql`, `ssh`, `rdp`, `ftp`, `vnc`): Auditoria Multiprocolo Híbrida Windows/Linux, Capturas de Tela RDP e Privileged Escalation.
- [[netexec-gerenciamento-banco-nxcdb-credenciais-hosts-exportacao]] — Veja também: NetExec (`nxcdb`): Consulta Estruturada do Banco de Dados de Auditoria (`hosts`, `creds`, `admin`, `shares`) e Reutilização por ID (`-id`).
- [[netexec-protocolo-smb-enumeracao-signing-shares-sessoes-disks]] — Referência cruzada direta com netexec-protocolo-smb-enumeracao-signing-shares-sessoes-disks.
- [[netexec-protocolo-ldap-kerberoasting-asreproast-bloodhound-delegacao]] — Referência cruzada direta com netexec-protocolo-ldap-kerberoasting-asreproast-bloodhound-delegacao.
- [[impacket-retransmissao-ntlmrelayx-smb-ldap-adcs-esc8-rbcd-shadow-credentials]] — Referência cruzada direta com impacket-retransmissao-ntlmrelayx-smb-ldap-adcs-esc8-rbcd-shadow-credentials.

## Fontes
- [NetExec Official GitHub — The Network Execution Tool (nxc & nxcdb)](https://raw.githubusercontent.com/Pennyw0rth/NetExec/main/README.md) — documentação oficial do NetExec cobrindo protocolos suportados, instalação via pipx e banco nxcdb; consultado em 2026-10-03.
- [NetExec Official Wiki — Getting Started & Protocol Usage](https://www.netexec.wiki/getting-started/installation) — wiki oficial do NetExec cobrindo instalação, autenticação Kerberos/NTLM, módulos e operação; consultado em 2026-10-03.
- [NetExec Official Repository](https://github.com/Pennyw0rth/NetExec) — repositório oficial do projeto NetExec; consultado em 2026-10-03.
