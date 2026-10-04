---
id: software.seguranca.tranche12.001125
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
fontes: ["https://raw.githubusercontent.com/mitre/caldera/master/README.md", "https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Controles de Furtividade (*Stealth*) em Operações do Caldera: **Obfuscators** (`plain-text`, `base64`, `caesar`, `steganography`), **Jitter** e **Autonomous Mode**

## Em uma frase
Quando você testa a maturidade de um SOC, executar todos os comandos em texto claro (`plain-text`) e com intervalos fixos de 5 segundos testa apenas o nível mais básico de detecção; e se o adversário codificar os comandos em Base64, aplicar ofuscação de strings e espaçar os beacons com *jitter* aleatório?

## Por que importa
Ao configurar uma **Operation** no Caldera, você controla três parâmetros críticos de furtividade (*Stealth*): **(1) `Obfuscator`** — transforma dinamicamente o comando de cada `link` antes de enviá-lo ao agente (suportando `plain-text`, `base64`, `base64jumble`, ` base64noPadding`, `caesar` cipher e `steganography`); **(2) `Jitter` (ex.: `4/8`)** — define o intervalo mínimo e máximo em segundos entre os check-ins dos agentes; e **(3) `Autonomous`** — define se a operação avança sozinha ou exige aprovação humana antes de cada `link`!

## Como funciona
Executar exatamente o mesmo *Adversary Profile* duas vezes — primeiro com `Obfuscator = plain-text` e depois com `Obfuscator = base64` — revela instantaneamente se as regras do seu SIEM são cegas para comandos codificados (ou se o seu **PowerShell Script Block Logging `EventID 4104`** e o **`hayabusa extract-base64`** estão cumprindo seu papel)!

## Exemplo
```bash
# Exemplo de chamada a API REST v2 do Caldera para listar todos os Obfuscators e Planners carregados no servidor
CALDERA_API_KEY="ADMIN123"
curl -sS -H "KEY: ${CALDERA_API_KEY}" http://127.0.0.1:8888/api/v2/obfuscators | jq '.[].name'
curl -sS -H "KEY: ${CALDERA_API_KEY}" http://127.0.0.1:8888/api/v2/planners | jq '.[].name'
```

## Limites e trade-offs
Em ambientes sensíveis ou durante sessões ao vivo de treinamento conjunto Red + Blue Team, desative o modo totalmente autônomo (**`autonomous: 0`**) na criação da operação para que o operador do Red Team aprove manualmente cada `link` gerado pelo Planner antes que o comando seja despachado ao endpoint.

## Como verificar
Sempre execute a etapa de *Cleanup* da operação (que roda os comandos de limpeza em ordem reversa) antes de encerrar os agentes.

## Conexões
- [[caldera-plugins-stockpile-emu-atomic-planos-ctid]] — Veja também: Bibliotecas de Ameaças do Caldera: Plugins **`stockpile`**, **`atomic`** e **`emu`** (Planos Oficiais do **MITRE CTID** — FIN6, APT29, Sandworm, LockBit).
- [[caldera-operacoes-blue-team-response-gameboard-purple-team]] — Veja também: Caldera para o **Blue Team e Purple Team**: Plugins **`response`**, **`gameboard`** e **`compass`** para Defesa Automatizada e Visualização Conjunta.
- [[caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins]] — Referência cruzada direta com caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins.
- [[caldera-agentes-sandcat-manx-ragdoll-c2-contacts-paw]] — Referência cruzada direta com caldera-agentes-sandcat-manx-ragdoll-c2-contacts-paw.
- [[hayabusa-extracao-base64-pivot-keywords-busca-regex-evtx]] — Referência cruzada direta com hayabusa-extracao-base64-pivot-keywords-busca-regex-evtx.

## Fontes
- [MITRE Caldera Official GitHub — Automated Adversary Emulation, Red Team & Incident Response Platform](https://raw.githubusercontent.com/mitre/caldera/master/README.md) — repositório oficial do MITRE Caldera v5 cobrindo o Core C2 Server, interface VueJS Magma e ecossistema de plugins (`sandcat`, `stockpile`, `atomic`, `emu`, `debrief`, `response`); consultado em 2026-10-03.
- [MITRE Caldera Official Documentation — Learning the Terminology (`Agents`, `Abilities`, `Adversaries`, `Operations`, `Planners`, `Facts`, `Parsers`)](https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html) — documentação oficial ReadTheDocs detalhando a arquitetura de planejamento orientado a fatos e agentes do Caldera; consultado em 2026-10-03.
