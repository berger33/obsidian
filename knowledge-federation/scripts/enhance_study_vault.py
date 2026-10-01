#!/usr/bin/env python3
from pathlib import Path
import zipfile, json, re
from kf_common import ROOT, now

VAULT = ROOT / "study-vault-1m-packs"
ZIP = ROOT / "archives" / "study-vault-1m-packs.zip"

def write_note(rel, title, body, tags):
    path = VAULT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    fm = "\n".join([
        "---",
        "tipo: guia",
        "status: curadoria",
        f"criado: {now()}",
        f"tags: [{', '.join(tags)}]",
        f"aliases: [\"{title}\"]",
        "---",
        f"# {title}",
        "",
    ])
    path.write_text(fm + body.strip() + "\n", encoding="utf-8")
    return path

TRILHAS = {
"20-Trilhas/Trilha-Orquestrador-de-IA.md": ("Trilha — Orquestrador de IA", """
## Objetivo
Formar repertório para dirigir agentes, avaliar saídas e transformar ideias em sistemas auditáveis.

## Ordem recomendada
1. [[MOC-vibe-coding-orquestracao]]
2. [[MOC-vibe-coding-context-engineering]]
3. [[MOC-ia-agentes]]
4. [[MOC-ia-rag]]
5. [[MOC-ia-avaliacao]]
6. [[MOC-vibe-coding-qualidade]]
7. [[MOC-software-testes]]
8. [[MOC-software-arquitetura]]

## Prática semanal
- Escolha 10 notas por semana.
- Para cada nota, gere uma pergunta, um teste, um risco e um critério de aceite.
- Use o agente apenas depois de escrever o objetivo em linguagem humana.

## Entregáveis esperados
- Briefing de projeto.
- Arquitetura mínima.
- Backlog validável.
- Suite de testes.
- Registro de decisões.
""", ["trilha", "ia", "orquestrador"]),
"20-Trilhas/Trilha-Fullstack-com-IA.md": ("Trilha — Fullstack com IA", """
## Objetivo
Construir apps, sites, APIs e automações usando IA sem perder controle técnico.

## Ordem recomendada
1. [[MOC-software-frontend]]
2. [[MOC-software-backend]]
3. [[MOC-software-arquitetura]]
4. [[MOC-software-testes]]
5. [[MOC-software-devops]]
6. [[MOC-ia-rag]]
7. [[MOC-vibe-coding-qualidade]]

## Checklist de projeto
- Problema e usuário-alvo definidos.
- Modelo de dados mínimo.
- API ou contrato de interface.
- Testes de regressão antes de refatorar.
- Deploy reproduzível.
- Observabilidade mínima.
""", ["trilha", "software", "fullstack"]),
"20-Trilhas/Trilha-Jogos-2D-Online-MMO.md": ("Trilha — Jogos 2D, Online e MMO", """
## Objetivo
Organizar estudo para jogos 2D, multiplayer e MMO com decisões técnicas graduais.

## Ordem recomendada
1. [[MOC-jogos-2d]]
2. [[MOC-jogos-game-design]]
3. [[MOC-jogos-netcode]]
4. [[MOC-jogos-mmo]]
5. [[MOC-software-backend]]
6. [[MOC-software-devops]]
7. [[MOC-ia-agentes]]

## Sequência de protótipos
- Protótipo local 2D.
- Protótipo com save/load.
- Protótipo online com poucas entidades.
- Teste de latência e reconexão.
- Simulação de economia/estado persistente.
- Vertical slice jogável.
""", ["trilha", "jogos", "mmo"]),
"20-Trilhas/Trilha-Produto-Carreira-MVP.md": ("Trilha — Produto, Carreira e MVP", """
## Objetivo
Transformar conhecimento técnico em produto, portfólio, carreira ou negócio.

## Ordem recomendada
1. [[MOC-negocio-mvp]]
2. [[MOC-negocio-carreira]]
3. [[MOC-vibe-coding-orquestracao]]
4. [[MOC-software-frontend]]
5. [[MOC-software-backend]]
6. [[MOC-ia-avaliacao]]

## Rotina de validação
- Escreva uma hipótese de valor.
- Defina o menor experimento observável.
- Faça uma landing page, protótipo ou demo.
- Colete evidência, não elogio genérico.
- Decida manter, mudar ou matar.
""", ["trilha", "produto", "carreira"]),
"20-Trilhas/Trilha-Ciencias-Reguladas-Seguras.md": ("Trilha — Ciências Reguladas com Segurança", """
## Objetivo
Estudar cannabis medicinal e micologia por uma lente documental, científica, ética e não operacional.

## Ordem recomendada
1. [[MOC-cannabis-documentacao-paciente]]
2. [[MOC-cannabis-estudos-clinicos]]
3. [[MOC-cannabis-qualidade-rastreabilidade]]
4. [[MOC-cannabis-riscos-interacoes]]
5. [[MOC-micologia-riscos-reducao-danos]]
6. [[MOC-micologia-cogumelos-medicinais-legais]]
7. [[MOC-micologia-taxonomia]]

> [!warning] Limite de uso
> Use esta trilha para organizar documentos, perguntas, leituras e conversas com profissionais habilitados. Não use como instrução de cultivo, extração, produção ou automedicação.

## Perguntas úteis
- Que evidência clínica existe?
- Quais riscos, interações e contraindicações precisam ser discutidos?
- Que documentos devem ser guardados?
- Qual profissional ou órgão regulatório deve ser consultado?
""", ["trilha", "seguranca", "regulado"]),
}

PLAYBOOKS = {
"30-Playbooks/Como-Estudar-Um-Pack.md": ("Playbook — Como estudar um pack", """
## Método em 5 passadas
1. **Varredura:** leia o MOC e marque 10 notas promissoras.
2. **Mapa:** escreva 5 conexões entre notas.
3. **Aplicação:** transforme 3 notas em tarefas práticas.
4. **Verificação:** adicione fontes primárias e data de acesso.
5. **Síntese:** crie uma nota própria com decisões e dúvidas.

## Prompts úteis
```text
Resuma esta nota separando fato, hipótese, opinião e risco. Sugira 3 fontes primárias para verificar.
```

```text
Transforme esta nota em checklist operacional seguro para desenvolvimento de software, sem inventar dados.
```
""", ["playbook", "estudo"]),
"30-Playbooks/Como-Materializar-Novos-Recortes.md": ("Playbook — Como materializar novos recortes", """
## Consultar antes
```bash
python knowledge-federation/scripts/query_checkpoint.py "termo" --domain ia --limit 20
```

## Materializar
```bash
python knowledge-federation/scripts/materialize_from_checkpoint.py \
  --domain software \
  --subdomain arquitetura \
  --limit 500 \
  --out checkpoint-materialized/software-arquitetura-extra \
  --zip archives/study-pack-software-arquitetura-extra.zip \
  --clean
```

## Recompilar vault
```bash
python knowledge-federation/scripts/build_study_vault.py
python knowledge-federation/scripts/enhance_study_vault.py
```
""", ["playbook", "ledger"]),
"30-Playbooks/Checklist-Fontes-e-Volatilidade.md": ("Checklist — Fontes e Volatilidade", """
## Antes de confiar
- A nota tem fonte primária?
- A informação muda com frequência?
- Existe preço, plano, limite, versão ou política?
- Há fonte independente confirmando?
- A fonte é marketing, fórum, opinião ou documentação oficial?

## Classificação rápida
- **Nível 1:** documentação oficial, legislação, bula, paper revisado, repositório oficial.
- **Nível 2:** artigo técnico com referências, relatório reconhecido.
- **Nível 3:** fórum, Reddit, HN, YouTube, post promocional.

## Regra prática
Se afeta decisão financeira, médica, jurídica, arquitetura ou segurança, verificar antes de aplicar.
""", ["playbook", "fontes"]),
"40-Decisao/Matriz-Ferramentas-IA-Dev.md": ("Matriz — Ferramentas de IA para Desenvolvimento", """
## Critérios
| Critério | Pergunta |
|---|---|
| Controle de código | A ferramenta mostra diff e permite revisão? |
| Contexto | Ela entende repo, issue, docs e histórico? |
| Segurança | Evita vazar segredos e comandos perigosos? |
| Custo | O preço e limites foram verificados em página oficial? |
| Reprodutibilidade | O resultado pode ser testado e repetido? |
| Integração | Funciona com terminal, IDE, CI/CD ou MCP? |

## Quando usar agente autônomo
Use quando há testes, escopo claro e rollback.

## Quando usar assistente pontual
Use quando o problema é pequeno, exploratório ou exige revisão humana intensa.
""", ["decisao", "ia", "ferramentas"]),
"40-Decisao/Matriz-Engine-Jogos.md": ("Matriz — Engine para Jogos", """
## Critérios
| Critério | Godot | Unity | Unreal | Web/Phaser |
|---|---|---|---|---|
| 2D | forte | forte | possível | forte |
| 3D | bom | forte | muito forte | limitado |
| MMO | exige backend próprio | exige backend próprio | exige backend próprio | exige backend próprio |
| Licença/custo | verificar licença MIT | verificar plano atual | verificar royalties/seats | verificar modelo atual |
| Aprendizado solo | bom | médio | mais pesado | bom para web |

## Regra prática
Escolha pela menor rota até o protótipo jogável, não pela engine mais poderosa.
""", ["decisao", "jogos"]),
"40-Decisao/Perguntas-Para-Profissionais-Regulados.md": ("Perguntas para profissionais em domínios regulados", """
## Para médico ou farmacêutico
- Quais objetivos terapêuticos são realistas?
- Quais interações medicamentosas precisam ser avaliadas?
- Como acompanhar efeitos, eventos adversos e evolução?
- Que documentação clínica deve ser guardada?

## Para advogado ou associação autorizada
- Que documentos comprovam autorização e conformidade?
- Quais limites legais mudam por estado, decisão ou regulamento?
- Como registrar rastreabilidade sem expor dados sensíveis?

## Para pesquisador ou especialista
- Quais fontes primárias são mais relevantes?
- Que evidências são preliminares ou controversas?
- Que afirmações comuns são hype?
""", ["decisao", "regulado", "seguranca"]),
}


def main():
    if not VAULT.exists():
        raise SystemExit("study-vault-1m-packs não existe. Rode build_study_vault.py primeiro.")
    for rel,(title,body,tags) in {**TRILHAS, **PLAYBOOKS}.items():
        write_note(rel, title, body, tags)

    home = VAULT / "00-Inicio" / "Home.md"
    text = home.read_text(encoding="utf-8")
    if "## Trilhas guiadas" not in text:
        insert = """
## Trilhas guiadas

- [[Trilha-Orquestrador-de-IA]]
- [[Trilha-Fullstack-com-IA]]
- [[Trilha-Jogos-2D-Online-MMO]]
- [[Trilha-Produto-Carreira-MVP]]
- [[Trilha-Ciencias-Reguladas-Seguras]]

## Playbooks e matrizes

- [[Como-Estudar-Um-Pack|Playbook — Como estudar um pack]]
- [[Como-Materializar-Novos-Recortes|Playbook — Como materializar novos recortes]]
- [[Checklist-Fontes-e-Volatilidade|Checklist — Fontes e Volatilidade]]
- [[Matriz-Ferramentas-IA-Dev|Matriz — Ferramentas de IA para Desenvolvimento]]
- [[Matriz-Engine-Jogos|Matriz — Engine para Jogos]]
- [[Perguntas-Para-Profissionais-Regulados|Perguntas para profissionais em domínios regulados]]

"""
        text = text.replace("## Mapas visuais\n", insert + "## Mapas visuais\n")
        home.write_text(text, encoding="utf-8")

    # Canvas extra para trilhas
    nodes=[{"id":"home","type":"file","file":"00-Inicio/Home.md","x":0,"y":0,"width":360,"height":140,"color":"1"}]
    edges=[]
    files=list(TRILHAS.keys())+list(PLAYBOOKS.keys())
    for i,rel in enumerate(files):
        nid=f"n{i}"
        nodes.append({"id":nid,"type":"file","file":rel,"x":((i%3)-1)*560,"y":260+(i//3)*240,"width":460,"height":130,"color":str((i%6)+1)})
        edges.append({"id":f"e{i}","fromNode":"home","toNode":nid})
    (VAULT / "_canvas" / "Trilhas-e-Playbooks.canvas").write_text(json.dumps({"nodes":nodes,"edges":edges}, ensure_ascii=False, indent=2), encoding="utf-8")

    if ZIP.exists(): ZIP.unlink()
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for f in VAULT.rglob("*"):
            if f.is_file():
                z.write(f, f.relative_to(ROOT))
    print(f"Enhancements adicionados ao vault: {VAULT}")
    print(f"Zip atualizado: {ZIP}")

if __name__ == "__main__":
    main()
