---
id: software.seguranca.tranche06.000600
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

# Detecção do NetExec pelo **Blue Team** (Correlação de Eventos Windows `4624`/`4625`/`5140`/`5145`/`4697`, Zeek e Hardening de Tiering AD)

## Em uma frase
Como o NetExec foi desenhado para varrer faixas de rede inteiras em alta velocidade, ele produz padrões claros de telemetria tanto na rede (**Zeek** / **Suricata**) quanto nos logs de segurança do Windows (**Event IDs `4624`, `4625`, `4768`, `4769`, `5140`, `5145`, `7045` e `4697`**).

## Por que importa
No nível de rede (**Zeek `conn.log` e `smb_mapping.log`**), um único endereço IP de origem abrindo dezenas de conexões TCP na porta `445` (ou `389`/`5985`/`1433`) em poucos segundos para múltiplos hosts da mesma sub-rede (*horizontal scan*) seguido por acessos ao `IPC$` e pipes RPC (`\pipe\srvsvc`, `\pipe\samr`, `\pipe\wkssvc`, `\pipe\atsvc`, `\pipe\svcctl`) é um indicador de altíssima fidelidade.

## Como funciona
No nível de arquitetura defensiva, a proteção mais eficaz contra a movimentação lateral demonstrada pelo NetExec combina: **(1) Windows LAPS** (senhas únicas para cada Administrador Local), **(2) Regras de Firewall de Host Windows** bloqueando tráfego de entrada nas portas `445/TCP`, `135/TCP`, `5985/TCP` e `3389/TCP` **entre estações de trabalho** (*Workstation-to-Workstation blocking*), **(3) Modelo de Tiering de Active Directory (Tier 0 / Tier 1 / Tier 2)** com *Authentication Policies & Authentication Policy Silos* e **(4) Grupo `Protected Users`** para todas as contas privilegiadas.

## Exemplo
```xml
<!-- Exemplo de consulta XPath no Windows Security Event Log para detectar acesso remoto a pipes administrativos via SMB (Event 5145) -->
<QueryList>
  <Query Id="0" Path="Security">
    <Select Path="Security">
      *[System[(EventID=5145)]]
      and
      *[EventData[Data[@Name='ShareName']='\\*\IPC$']]
      and
      *[EventData[Data[@Name='RelativeTargetName']='svcctl' or Data[@Name='RelativeTargetName']='atsvc' or Data[@Name='RelativeTargetName']='samr']]
    </Select>
  </Query>
</QueryList>
```

## Limites e trade-offs
Contas adicionadas ao grupo de segurança nativo **`Protected Users`** do Active Directory não podem autenticar via NTLM, não podem usar cifras DES/RC4 no Kerberos, não armazenam credenciais em cache na memória após o logoff e têm tempo de vida reduzido de TGT.

## Como verificar
Teste adicionar uma conta de laboratório ao grupo `Protected Users` e confirme que tentativas de autenticação com hash NTLM (`nxc smb ... -H <NTHASH>`) são imediatamente bloqueadas pelo Domain Controller.

## Conexões
- [[netexec-gerenciamento-banco-nxcdb-credenciais-hosts-exportacao]] — Veja também: NetExec (`nxcdb`): Consulta Estruturada do Banco de Dados de Auditoria (`hosts`, `creds`, `admin`, `shares`) e Reutilização por ID (`-id`).
- [[netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces]] — Referência cruzada direta com netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces.
- [[responder-defesa-hardening-gpo-desativar-llmnr-nbtns-wpad-smb-signing]] — Referência cruzada direta com responder-defesa-hardening-gpo-desativar-llmnr-nbtns-wpad-smb-signing.
- [[timesketch-deteccao-ameacas-regras-sigma-tsctl-sigma-analyzer]] — Referência cruzada direta com timesketch-deteccao-ameacas-regras-sigma-tsctl-sigma-analyzer.

## Fontes
- [NetExec Official GitHub — The Network Execution Tool (nxc & nxcdb)](https://raw.githubusercontent.com/Pennyw0rth/NetExec/main/README.md) — documentação oficial do NetExec cobrindo protocolos suportados, instalação via pipx e banco nxcdb; consultado em 2026-10-03.
- [NetExec Official Wiki — Getting Started & Protocol Usage](https://www.netexec.wiki/getting-started/installation) — wiki oficial do NetExec cobrindo instalação, autenticação Kerberos/NTLM, módulos e operação; consultado em 2026-10-03.
- [NetExec Official Repository](https://github.com/Pennyw0rth/NetExec) — repositório oficial do projeto NetExec; consultado em 2026-10-03.
