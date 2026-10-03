---
id: software.seguranca.tranche06.000578
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

# Auditoria de Força de Senhas sobre Hashes Capturados pelo Responder (`NetNTLMv2` Hashcat `-m 5600` vs `NetNTLMv1` `-m 5500`)

## Em uma frase
Os arquivos gerados pelo Responder em `logs/*-NTLMv2-*.txt` e `logs/*-NTLMv1-*.txt` permitem auditar a resistência das senhas dos usuários e contas de serviço do domínio contra ataques offline de dicionário e regras usando **Hashcat** (`-m 5600` e `-m 5500`).

## Por que importa
Existe uma diferença criptográfica abissal entre **NetNTLMv1 (`-m 5500`)** e **NetNTLMv2 (`-m 5600`)**: se uma máquina legada ainda permite enviar respostas **NetNTLMv1 / LM**, e o `Challenge` de 8 bytes no `Responder.conf` for configurado como `1122334455667788`, o hash DES do NetNTLMv1 pode ser revertido matematicamente para o **hash NTLM puro (`MD4(UTF-16LE(password))`)** independentemente do tamanho da senha (permitindo *Pass-the-Hash* imediato!).

## Como funciona
Por isso, o `Responder.conf` usa `Challenge = Random` por padrão (para evitar detecção por assinaturas estáticas de NIDS que procuram pelo challenge fixo `1122334455667788`) e permite definir um challenge fixo apenas quando se audita especificamente a presença crítica de clientes **NetNTLMv1**.

## Exemplo
```bash
# Auditar hashes NetNTLMv2 capturados no Responder contra dicionario corporativo e regras basicas no Hashcat
hashcat -m 5600 /opt/Responder/logs/SMB-NTLMv2-SSP-10.10.20.55.txt \
  /opt/secops/wordlists/corp_audit.dict \
  -r /usr/share/hashcat/rules/best64.rule --status
```

## Limites e trade-offs
Garanta que todas as máquinas do domínio estejam configuradas via GPO com **LAN Manager authentication level = `Send NTLMv2 response only. Refuse LM & NTLM`** (`LmCompatibilityLevel = 5`), eliminando 100% do risco de downgrade para NetNTLMv1.

## Como verificar
Verifique no diretório `logs/` do Responder que nenhum arquivo `*-NTLMv1-*` foi gerado durante o teste.

## Conexões
- [[responder-utilitarios-runfinger-findsqlsrv-icmp-redirect-multirelay]] — Veja também: Ferramentas Auxiliares da Suíte Responder (`tools/RunFinger.py`, `tools/FindSQLSrv.py` e `tools/MultiRelay.py`).
- [[responder-deteccao-blue-team-suricata-zeek-sysmon-canary-queries]] — Veja também: Detecção de Envenenamento LLMNR/NBT-NS/mDNS/DHCPv6 pelo **Blue Team** (Suricata, Zeek, Windows Event Logs e *Canary Name Queries*).
- [[responder-servidores-autenticacao-rogue-smb-http-ldap-mssql-ntlmv2]] — Referência cruzada direta com responder-servidores-autenticacao-rogue-smb-http-ldap-mssql-ntlmv2.
- [[responder-defesa-hardening-gpo-desativar-llmnr-nbtns-wpad-smb-signing]] — Referência cruzada direta com responder-defesa-hardening-gpo-desativar-llmnr-nbtns-wpad-smb-signing.

## Fontes
- [Responder Official GitHub — LLMNR/NBT-NS/mDNS/DHCPv6 Poisoner & Rogue Servers](https://raw.githubusercontent.com/lgandx/Responder/master/README.md) — documentação oficial do Responder cobrindo modo passivo -A, servidores rogue, DHCPv6, Kerberos e ferramentas auxiliares; consultado em 2026-10-03.
- [Responder Official Configuration — Responder.conf Reference](https://raw.githubusercontent.com/lgandx/Responder/master/Responder.conf) — configuração oficial do Responder detalhando KerberosMode, RespondTo, DontRespondTo, AutoIgnoreAfterSuccess e DHCPv6; consultado em 2026-10-03.
- [Responder Repository & Tools Suite](https://github.com/lgandx/Responder) — repositório oficial da suíte Responder (RunFinger, MultiRelay, FindSQLSrv); consultado em 2026-10-03.
