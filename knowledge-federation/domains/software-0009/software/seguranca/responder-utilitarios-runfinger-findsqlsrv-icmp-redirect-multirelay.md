---
id: software.seguranca.tranche06.000577
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
fontes: ["https://raw.githubusercontent.com/lgandx/Responder/master/README.md", "https://raw.githubusercontent.com/lgandx/Responder/master/Responder.conf", "https://github.com/lgandx/Responder"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ferramentas Auxiliares da Suíte Responder (`tools/RunFinger.py`, `tools/FindSQLSrv.py` e `tools/MultiRelay.py`)

## Em uma frase
O diretório **`tools/`** do repositório oficial do Responder fornece utilitários focados em reconhecimento rápido de serviços Microsoft e demonstração de retransmissão NTLM: **`RunFinger.py`**, **`FindSQLSrv.py`** e **`MultiRelay.py`**.

## Por que importa
O **`RunFinger.py`** envia pacotes mínimos de negociação SMB1/SMB2 e RDP para uma faixa CIDR inteira em poucos segundos, extraindo o *Build Number* exato do Windows, o skew de relógio (útil para Kerberos), se o host exige `SMB Signing` e se o serviço `RemoteRegistry` ou `MSSQL` está acessível.

## Como funciona
Já o **`FindSQLSrv.py`** envia um pacote UDP de descoberta para a porta `1434` (*SQL Server Browser Service*) na rede para localizar todas as instâncias nomeadas de Microsoft SQL Server, suas versões e as portas TCP dinâmicas em que cada instância está escutando.

## Exemplo
```bash
# Descobrir hosts sem SMB Signing na rede com RunFinger.py e localizar instancias MSSQL via UDP 1434
python3 /opt/Responder/tools/RunFinger.py -i 10.10.20.0/24
python3 /opt/Responder/tools/FindSQLSrv.py
```

## Limites e trade-offs
O serviço *SQL Server Browser* (UDP 1434) anuncia em claro os nomes das instâncias e números de porta; em ambientes de alta segurança com portas TCP fixas configuradas no SQL Server Configuration Manager, o serviço *SQL Server Browser* pode ser desabilitado.

## Como verificar
Valide os resultados do `RunFinger.py` cruzando a lista de hosts encontrados com o inventário oficial de ativos de TI daquela VLAN.

## Conexões
- [[responder-fluxo-ntlm-relay-desativar-smb-http-ntlmrelayx-multirelay]] — Veja também: Responder & `ntlmrelayx.py`: Desativação dos Servidores `SMB` e `HTTP` no `Responder.conf` para **NTLM Relay** em Tempo Real.
- [[responder-auditoria-offline-senhas-hashcat-netntlmv2-netntlmv1-regras]] — Veja também: Auditoria de Força de Senhas sobre Hashes Capturados pelo Responder (`NetNTLMv2` Hashcat `-m 5600` vs `NetNTLMv1` `-m 5500`).
- [[impacket-cliente-mssqlclient-xp-cmdshell-linked-servers-trusted-links]] — Referência cruzada direta com impacket-cliente-mssqlclient-xp-cmdshell-linked-servers-trusted-links.
- [[netexec-protocolos-mssql-ssh-rdp-ftp-vnc-auditoria-multi-servico]] — Referência cruzada direta com netexec-protocolos-mssql-ssh-rdp-ftp-vnc-auditoria-multi-servico.

## Fontes
- [Responder Official GitHub — LLMNR/NBT-NS/mDNS/DHCPv6 Poisoner & Rogue Servers](https://raw.githubusercontent.com/lgandx/Responder/master/README.md) — documentação oficial do Responder cobrindo modo passivo -A, servidores rogue, DHCPv6, Kerberos e ferramentas auxiliares; consultado em 2026-10-03.
- [Responder Official Configuration — Responder.conf Reference](https://raw.githubusercontent.com/lgandx/Responder/master/Responder.conf) — configuração oficial do Responder detalhando KerberosMode, RespondTo, DontRespondTo, AutoIgnoreAfterSuccess e DHCPv6; consultado em 2026-10-03.
- [Responder Repository & Tools Suite](https://github.com/lgandx/Responder) — repositório oficial da suíte Responder (RunFinger, MultiRelay, FindSQLSrv); consultado em 2026-10-03.
