---
id: software.seguranca.tranche12.001109
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/README.md", "https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/Cargo.toml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Investigação de **Movimentação Lateral, Brute-Force e Escalação de Privilégio** (`lateral_movement` e `security`) com o Chainsaw

## Em uma frase
Ao investigar um ataque de intrusão humana (*Human-Operated Ransomware*), três perguntas precisam ser respondidas rapidamente em cada servidor coletado: **(1)** De qual endereço IP de origem o invasor entrou neste host?; **(2)** Houve tentativa de força bruta ou *password spraying*?; e **(3)** O atacante criou contas de backdoor ou adicionou usuários ao grupo `Administrators` / `Domain Admins`?

## Por que importa
O conjunto de regras nativas do Chainsaw em `rules/lateral_movement/` e `rules/security/` responde a essas três perguntas diretamente sobre o `Security.evtx`, `Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx` e `Microsoft-Windows-RemoteDesktopServices-RdpCoreTS%4Operational.evtx`!

## Como funciona
Ele agrupa e destaca logins remotos bem-sucedidos (Logon Types `3` Network, `7` Unlock, `9` NewCredentials / Pass-the-Hash com `seclogo`, `10` RemoteInteractive RDP), sessões de reconexão RDP (`EventID 21, 24, 25`), rajadas de falhas de autenticação (`EventID 4625`) e adições a grupos de segurança locais/globais (`EventID 4728, 4732, 4756`)!

## Exemplo
```bash
# Executar triagem focada em Movimentacao Lateral e Alteracoes de Contas/Grupos em um servidor comprometido
chainsaw hunt ./evtx_servidor_alvo/ \
  -r ./chainsaw/rules/lateral_movement/ \
  -r ./chainsaw/rules/security/ \
  --metadata --full
```

## Limites e trade-offs
Atenção especial ao **Logon Type `9` (`NewCredentials`)** no `EventID 4624`: quando um atacante executa **Pass-the-Hash** ou **Overpass-the-Hash** (por exemplo, `sekurlsa::pth` no Mimikatz ou `runas /netonly`), o Windows registra um `EventID 4624` com `LogonType = 9` e `LogonProcessName = seclogo`!

## Como verificar
Combine a saída de movimentação lateral do Chainsaw com o `hayabusa logon-summary` para construir o mapa completo de pivôs de rede entre os hosts da organização.

## Conexões
- [[chainsaw-autoria-regras-customizadas-tau-filter-document-fields]] — Veja também: Autoria de **Regras Nativas do Chainsaw** e Mapeamentos Customizados no Formato **TAU Engine** (`filter`, `group`, `fields`).
- [[chainsaw-workflow-integrado-chainsaw-hayabusa-kape-velociraptor-dfir]] — Veja também: Playbook Integrado **Chainsaw + Hayabusa** em DFIR: Como Combinar o Melhor dos Dois Motores Rust na Triagem Forense Windows.
- [[chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust]] — Referência cruzada direta com chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust.
- [[chainsaw-regras-nativas-av-alerts-defender-sophos-kaspersky-evtx]] — Referência cruzada direta com chainsaw-regras-nativas-av-alerts-defender-sophos-kaspersky-evtx.
- [[hayabusa-comandos-analise-metricas-logon-summary-critical-systems]] — Referência cruzada direta com hayabusa-comandos-analise-metricas-logon-summary-critical-systems.

## Fontes
- [WithSecure Chainsaw Official GitHub — Rapidly Search and Hunt Through Windows Forensic Artefacts](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/README.md) — repositório oficial do Chainsaw cobrindo triagem forense (`hunt`, `search`, `analyse shimcache`, `analyse srum`, `dump`), regras Sigma e motor TAU; consultado em 2026-10-03.
- [WithSecure Chainsaw Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/Cargo.toml) — especificação oficial das bibliotecas forenses em Rust do Chainsaw 2.16+ (`evtx`, `mft`, `notatin`, `libesedb`, `tau-engine`, `aho-corasick`, `rayon`); consultado em 2026-10-03.
