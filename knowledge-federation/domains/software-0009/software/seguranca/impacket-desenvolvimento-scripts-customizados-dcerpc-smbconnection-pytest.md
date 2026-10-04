---
id: software.seguranca.tranche06.000590
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
fontes: ["https://raw.githubusercontent.com/fortra/impacket/master/README.md", "https://raw.githubusercontent.com/fortra/impacket/master/TESTING.md", "https://github.com/fortra/impacket"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Impacket: Desenvolvimento de Scripts de Auditoria em Python com `SMBConnection` e `DCERPCTransportFactory`, e Suíte de Testes `pytest` / `tox`

## Em uma frase
Além de usar os exemplos prontos de linha de comando, engenheiros de segurança e pesquisadores de vulnerabilidades importam diretamente os pacotes `impacket.smbconnection.SMBConnection` e `impacket.dcerpc.v5.transport.DCERPCTransportFactory` para escrever verificadores customizados de protocolos Microsoft.

## Por que importa
Quando a Microsoft publica um boletim de segurança em um serviço RPC específico (como o *Print Spooler* `[MS-RPRN]`, *Task Scheduler* `[MS-TSCH]` ou *Certificate Services* `[MS-ICPR]`), a camada de transporte RPC do Impacket cuida automaticamente da autenticação SMB/Kerberos, fragmentação de pacotes PDU, *DCERPC Bind* para o UUID da interface e serialização NDR (*Network Data Representation*).

## Como funciona
Conforme documentado em `TESTING.md` do repositório oficial, o projeto mantém uma suíte abrangente de testes automatizados dividida entre testes offline (`pytest -m "not remote"`) e testes de integração contra um laboratório Active Directory (`pytest -m "remote"`), orquestrada com `tox` e `pytest-cov`.

## Exemplo
```python
from impacket.dcerpc.v5 import transport, scmr

# Conectar programaticamente ao pipe \pipe\svcctl (MS-SCMR) via SMB usando o transporte DCERPC do Impacket
string_binding = r"ncacn_np:10.10.20.55[\pipe\svcctl]"
rpctransport = transport.DCERPCTransportFactory(string_binding)
rpctransport.set_kerberos(True)
dce = rpctransport.get_dce_rpc()
dce.connect()
dce.bind(scmr.MSRPC_UUID_SCMR)
dce.disconnect()
```

## Limites e trade-offs
Conforme alerta o `TESTING.md` oficial do Impacket, testes remotos (`pytest -m "remote"`) que criam ou modificam contas e objetos no Active Directory de laboratório não são idempotentes caso interrompidos no meio; tire sempre um snapshot da VM do Domain Controller de laboratório antes de rodar a suíte remota.

## Como verificar
Execute `pytest -m "not remote" -k "ldap"` no repositório do Impacket para validar os testes unitários locais de serialização ASN.1/LDAP.

## Conexões
- [[impacket-gestao-contas-acl-addcomputer-dacledit-rbcd-laps-dpapi]] — Veja também: Impacket: Auditoria de Objetos de Diretório e Criptografia (`addcomputer.py`, `dacledit.py`, `rbcd.py`, `GetLAPSPassword.py` e **`dpapi.py`**).
- [[impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos]] — Referência cruzada direta com impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos.
- [[impacket-enumeracao-msrpc-rpcdump-samrdump-lookupsid-netview-services]] — Referência cruzada direta com impacket-enumeracao-msrpc-rpcdump-samrdump-lookupsid-netview-services.
- [[netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces]] — Referência cruzada direta com netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces.

## Fontes
- [Fortra Impacket Official GitHub — Network Protocols & Examples Overview](https://raw.githubusercontent.com/fortra/impacket/master/README.md) — documentação oficial do Fortra Impacket cobrindo protocolos SMB1-3, MSRPC, Kerberos, LDAP, TDS e utilitários; consultado em 2026-10-03.
- [Fortra Impacket Official Testing Guide — TESTING.md & AD Lab Setup](https://raw.githubusercontent.com/fortra/impacket/master/TESTING.md) — guia oficial de testes locais/remotos (pytest, tox) e configuração de laboratório Active Directory e LDAPS; consultado em 2026-10-03.
- [Fortra Impacket Official Repository](https://github.com/fortra/impacket) — repositório oficial da biblioteca Impacket; consultado em 2026-10-03.
