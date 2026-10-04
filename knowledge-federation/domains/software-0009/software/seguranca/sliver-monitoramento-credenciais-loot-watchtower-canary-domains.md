---
id: software.seguranca.tranche16.001548
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/BishopFox/sliver/master/README.md", "https://sliver.sh/docs?name=Getting+Started"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Gestão de Credenciais (**`loot`**), Monitoramento Contínuo de Vazamento de Implantes (**`Watchtower` — VirusTotal / XForce**) e **Canary Domains** no Sliver

## Em uma frase
Durante um exercício prolongado de Red Team, como a equipe compartilha de forma segura chaves SSH, tickets Kerberos, dumps de configuração e senhas capturadas sem espalhar arquivos sensíveis nas máquinas locais dos operadores, e como o Sliver avisa imediatamente se o Blue Team ou um antivírus enviou o seu implante para o **VirusTotal**?

## Por que importa
Através de dois subsistemas integrados do Sliver: **(1) Cofre Centralizado `loot`** — armazena no servidor (e sincroniza com todos os operadores no modo Multiplayer!) arquivos e credenciais capturados durante a operação (`loot add`, `loot fetch`, `loot ls`); e **(2) O serviço `Watchtower`**!

## Como funciona
Quando você configura o **`Watchtower`** no Sliver informando uma chave de API do **VirusTotal** (ou IBM X-Force), o servidor Sliver **consulta periodicamente apenas os hashes SHA-256 dos implantes gerados na operação** — se algum hash aparecer no VirusTotal, o Sliver dispara um alerta imediato no console de todos os operadores informando que aquele binário foi descoberto e enviado para análise na nuvem!

## Exemplo
```text
# Inspecionar o cofre centralizado de artefatos/credenciais (loot) e verificar os dominios canario (canaries) no console do Sliver
sliver > loot
sliver > canaries
sliver > implants
```

## Limites e trade-offs
Por que o **`Watchtower`** consulta no VirusTotal **apenas o hash SHA-256** (nunca enviando o arquivo binário em si!) e como os **Canary Domains (`canaries`)** complementam essa detecção? Quando uma amostra de malware é submetida a um sandbox público ou analisada pelo SOC, o sandbox executa o binário e tenta resolver os domínios contidos nele: se o servidor DNS do Sliver detectar uma consulta a um **Canary Domain** específico daquele implante, o comando `canaries` marca aquele implante como **Queimado (`Triggered`)**!

## Como verificar
Ao final do exercício de Red Team, limpe e destrua de forma segura todos os artefatos do cofre `loot` e forneça a lista completa de hashes SHA-256 de `implants` para a equipe do SOC validar seus IOCs.

## Conexões
- [[sliver-compilacao-ofuscacao-garble-stagers-shellcode-external-builders]] — Veja também: Compilação Avançada de Implantes no Sliver: Ofuscação de Símbolos (**`garble`**), Formatos (`executable`, `shared-lib`, `service`, `shellcode`), **Stagers** e **External Builders**.
- [[sliver-extensao-cursed-chrome-electron-debug-port-post-exploitation]] — Veja também: Pós-Exploração de Navegadores e Apps **Electron (`Slack`, `VS Code`, `Teams`, `Discord`)** com o Subsistema **`cursed`** do Sliver.
- [[sliver-arquitetura-c2-emulacao-adversarios-mtls-wireguard-http-dns]] — Referência cruzada direta com sliver-arquitetura-c2-emulacao-adversarios-mtls-wireguard-http-dns.
- [[sliver-modo-multiplayer-operadores-grpc-mtls-rbac-auditoria-logs]] — Referência cruzada direta com sliver-modo-multiplayer-operadores-grpc-mtls-rbac-auditoria-logs.

## Fontes
- [Sliver Adversary Emulation Framework Official Repository (`BishopFox/sliver`)](https://raw.githubusercontent.com/BishopFox/sliver/master/README.md) — repositório oficial do framework C2 Sliver em Go cobrindo implantes multi-plataforma, chaves assimétricas únicas por binário e execução BOF/COFF; consultado em 2026-10-03.
- [Sliver Official Documentation — Getting Started (`sliver.sh/docs?name=Getting+Started`)](https://sliver.sh/docs?name=Getting+Started) — documentação oficial do Sliver detalhando arquitetura Server/Multiplayer, diferença entre `Beacon Mode` e `Session Mode`, geração de implantes, `interactive` e Stagers; consultado em 2026-10-03.
