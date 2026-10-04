---
id: software.seguranca.tranche06.000591
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

# NetExec (`nxc` & `nxcdb`): Arquitetura do Sucessor Open-Source do CrackMapExec, Protocolos Suportados e Isolamento por *Workspaces*

## Em uma frase
**NetExec (`nxc`)** (`Pennyw0rth/NetExec`, BSD-2-Clause, Python 3.10+) é a ferramenta de avaliação de segurança e auditoria em escala de redes Active Directory e ambientes corporativos multiprocolo, criada e mantida pela comunidade como sucessora direta do projeto CrackMapExec.

## Por que importa
Permite avaliar centenas de servidores e estações em segundos através de **9 protocolos nativos** (**`smb`**, **`ldap`**, **`winrm`**, **`wmi`**, **`mssql`**, **`rdp`**, **`ssh`**, **`ftp`** e **`vnc`**), correlacionando automaticamente todos os hosts, serviços, compartilhamentos e credenciais descobertas no banco de dados relacional **`nxcdb`**.

## Como funciona
Cada engajamento ou cliente deve ser isolado em um **Workspace** próprio dentro do `nxcdb` (`~/.nxc/workspaces/<nome>/`), onde cada protocolo mantém seu banco SQLite estruturado (`smb.db`, `ldap.db`, `mssql.db`, `ssh.db`), permitindo consultar credenciais validadas, relações de administração local (`AdminRelations`) e exportar relatórios sem misturar dados de auditorias diferentes.

## Exemplo
```bash
# Instalar o NetExec isolado via pipx, verificar os protocolos disponiveis e criar um workspace para a auditoria
pipx install git+https://github.com/Pennyw0rth/NetExec
nxc --version
nxcdb -e "create workspace pentest_q4_2026"
```

## Limites e trade-offs
Sempre instale o NetExec através do **`pipx`** (`pipx install git+https://github.com/Pennyw0rth/NetExec`) para isolar suas dependências exatas do Impacket, `pypykatz`, `bloodhound-python` e `minikerberos` sem conflitar com pacotes Python globais do sistema.

## Como verificar
Abra o utilitário **`nxcdb`** e execute `workspace` e `hosts` para inspecionar o banco de dados do workspace ativo.

## Conexões
- [[netexec-protocolo-smb-enumeracao-signing-shares-sessoes-disks]] — Veja também: NetExec (`nxc smb`): Mapeamento de Sub-Redes SMB, Verificação de `signing:False` / `SMBv1:True`, Compartilhamentos (`--shares`) e Sessões (`--sessions`).
- [[netexec-gerenciamento-banco-nxcdb-credenciais-hosts-exportacao]] — Referência cruzada direta com netexec-gerenciamento-banco-nxcdb-credenciais-hosts-exportacao.
- [[impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos]] — Referência cruzada direta com impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos.

## Fontes
- [NetExec Official GitHub — The Network Execution Tool (nxc & nxcdb)](https://raw.githubusercontent.com/Pennyw0rth/NetExec/main/README.md) — documentação oficial do NetExec cobrindo protocolos suportados, instalação via pipx e banco nxcdb; consultado em 2026-10-03.
- [NetExec Official Wiki — Getting Started & Protocol Usage](https://www.netexec.wiki/getting-started/installation) — wiki oficial do NetExec cobrindo instalação, autenticação Kerberos/NTLM, módulos e operação; consultado em 2026-10-03.
- [NetExec Official Repository](https://github.com/Pennyw0rth/NetExec) — repositório oficial do projeto NetExec; consultado em 2026-10-03.
